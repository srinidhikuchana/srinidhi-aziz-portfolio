import os
from flask import Flask, render_template
from dotenv import load_dotenv
from peewee import *
from app import data

load_dotenv()

app = Flask(__name__)

db = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST")
)
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
