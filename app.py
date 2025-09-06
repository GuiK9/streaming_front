from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, template_folder='app/templates')
app.config['DOMAIN_API'] = os.getenv('DOMAIN_API')

from app.routes import main
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)