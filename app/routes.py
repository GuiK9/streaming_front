
from flask import Blueprint, render_template
import requests
import os

main = Blueprint('main', __name__)

@main.route('/')
def hello():
    try:
        print(os.getenv('DOMAIN_API') + '/api/videos')
        response = requests.get(os.getenv('DOMAIN_API') + '/api/videos')
        videos = response.json() if response.status_code == 200 else []
    except Exception as e:
        print(f"Error fetching videos: {e}")
        videos = []
    return render_template('index.html', videos=videos)

@main.route('/about')
def about():
    return render_template('about.html')
