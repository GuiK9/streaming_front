from flask import Flask
from app.routes import main
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config['LINK_SITE'] = os.getenv('LINK_SITE')
    app.config['API_URL'] = os.getenv('API_URL')
    return app
