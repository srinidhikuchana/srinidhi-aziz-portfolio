import datetime
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from peewee import (
    CharField,
    DateTimeField,
    Model,
    MySQLDatabase,
    TextField,
)
from playhouse.shortcuts import model_to_dict

from app import data


load_dotenv()

app = Flask(__name__)


# MySQL database connection
mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


# Connect and create the table if it does not already exist.
mydb.connect(reuse_if_open=True)
mydb.create_tables([TimelinePost], safe=True)

print(mydb)


@app.route("/")
def index():
    return render_template(
        "homepage.html",
        title="Team Portfolio",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="index",
        team_members=data.TEAM_MEMBERS,
    )


@app.route("/sri-nidhi")
def sri_nidhi():
    return render_template(
        "index.html",
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


@app.route("/hobbies")
@app.route("/sri-nidhi/hobbies")
def sri_nidhi_hobbies():
    return render_template(
        "hobbies.html",
        title="Sri Nidhi Hobbies",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="sri_nidhi_hobbies",
        hobbies=data.HOBBIES,
    )


@app.route("/aziz")
def aziz():
    return render_template(
        "aziz.html",
        title="Aziz Ercoban",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="aziz",
        about_me=data.AZIZ_ABOUT_ME,
        experiences=data.AZIZ_EXPERIENCES,
        education=data.AZIZ_EDUCATION,
        travel_places=data.AZIZ_TRAVEL_PLACES,
    )


@app.route("/aziz/hobbies")
def aziz_hobbies():
    return render_template(
        "aziz_hobbies.html",
        title="Aziz Hobbies",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="aziz_hobbies",
        hobbies=data.AZIZ_HOBBIES,
    )


@app.route("/api/timeline_post", methods=["POST"])
def post_timeline_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]

    timeline_post = TimelinePost.create(
        name=name,
        email=email,
        content=content,
    )

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_timeline_posts():
    return {
        "timeline_posts": [
            model_to_dict(post)
            for post in TimelinePost.select().order_by(
                TimelinePost.created_at.desc()
            )
        ]
    }