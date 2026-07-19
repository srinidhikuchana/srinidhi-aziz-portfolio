import os
import datetime
import re
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
from app import data

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    db = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    db = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST")
    )


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


db.connect()
db.create_tables([TimelinePost], safe=True)


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/api/timeline_post', methods=['POST'])
def create_timeline_post():
    req_data = request.get_json(silent=True)
    if not isinstance(req_data, dict):
        req_data = {}

    name = req_data.get('name')
    if not isinstance(name, str) or not name.strip():
        return jsonify({'error': 'Invalid name'}), 400

    content = req_data.get('content')
    if not isinstance(content, str) or not content.strip():
        return jsonify({'error': 'Invalid content'}), 400

    email = req_data.get('email')
    if not isinstance(email, str) or not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', email.strip()):
        return jsonify({'error': 'Invalid email'}), 400

    post = TimelinePost.create(
        name=name.strip(),
        email=email.strip(),
        content=content.strip()
    )
    return jsonify(model_to_dict(post)), 201


@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_posts():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return jsonify({'timeline_posts': [model_to_dict(p) for p in posts]}), 200


@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_timeline_post(post_id):
    post = TimelinePost.get_or_none(TimelinePost.id == post_id)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    post.delete_instance()
    return jsonify({'message': 'Post deleted', 'id': post_id}), 200


@app.route('/')
def index():
    return render_template(
        'homepage.html',
        title="Team Portfolio",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="index",
        team_members=data.TEAM_MEMBERS,
    )


@app.route('/sri-nidhi')
def sri_nidhi():
    return render_template(
        'index.html',
        title="Sri Nidhi Kuchana",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="sri_nidhi",
        about_me=data.ABOUT_ME,
        experiences=data.EXPERIENCES,
        education=data.EDUCATION,
        travel_places=data.TRAVEL_PLACES,
        google_maps_api_key=os.getenv("GOOGLE_MAPS_API_KEY"),
    )


@app.route('/hobbies')
@app.route('/sri-nidhi/hobbies')
def sri_nidhi_hobbies():
    return render_template(
        'hobbies.html',
        title="Sri Nidhi Hobbies",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="sri_nidhi_hobbies",
        hobbies=data.HOBBIES,
    )


@app.route('/aziz')
def aziz():
    return render_template(
        'aziz.html',
        title="Aziz Ercoban",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="aziz",
        about_me=data.AZIZ_ABOUT_ME,
        experiences=data.AZIZ_EXPERIENCES,
        education=data.AZIZ_EDUCATION,
        travel_places=data.AZIZ_TRAVEL_PLACES,
    )


@app.route('/aziz/hobbies')
def aziz_hobbies():
    return render_template(
        'aziz_hobbies.html',
        title="Aziz Hobbies",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="aziz_hobbies",
        hobbies=data.AZIZ_HOBBIES,
    )
