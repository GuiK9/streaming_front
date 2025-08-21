from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['DOMAIN_API'] = os.getenv('DOMAIN_API')
    from .routes import main
    app.register_blueprint(main)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
