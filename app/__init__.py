import os
from flask import Flask, render_template
from dotenv import load_dotenv

from app import data

load_dotenv()
app = Flask(__name__)


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
        'coming_soon.html',
        title="Aziz Ercoban",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="aziz",
        page_title="Aziz Ercoban",
        message="Aziz's portfolio page will be added in the next branch.",
    )


@app.route('/aziz/hobbies')
def aziz_hobbies():
    return render_template(
        'coming_soon.html',
        title="Aziz Hobbies",
        url=os.getenv("URL"),
        nav_links=data.NAV_LINKS,
        active_page="aziz_hobbies",
        page_title="Aziz Hobbies",
        message="Aziz's hobbies page will be added in a later branch.",
    )