import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

from app import data

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="Sri Nidhi Kuchana",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="index",
        about_me=data.ABOUT_ME,
        experiences=data.EXPERIENCES,
        education=data.EDUCATION,
        travel_places=data.TRAVEL_PLACES,
        google_maps_api_key=os.getenv("GOOGLE_MAPS_API_KEY"),
    )


@app.route('/hobbies')
def hobbies():
    return render_template(
        'hobbies.html',
        title="Hobbies",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="hobbies",
        hobbies=data.HOBBIES,
    )