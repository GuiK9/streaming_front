from flask import Blueprint, render_template, request
import requests
import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
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

@main.route('/upload', methods=['POST'])
def upload():
    metadata_json = request.form.get('metadata')
    video_file = request.files.get('video')

    if not metadata_json or not video_file:
        return "Metadata ou vídeo não enviados.", 400

    files = {
        'metadata': (None, metadata_json, 'application/json'),
        'video': (video_file.filename, video_file.stream, video_file.mimetype)
    }

    try:
        response = requests.post(
            'http://localhost/api/videos',
            files=files
        )
        if response.status_code == 201:
            return "Vídeo enviado com sucesso!", 201
        else:
            return f"Erro ao enviar vídeo: {response.text}", response.status_code
    except Exception as e:
        return f"Erro ao conectar à API: {e}",

@main.route('/cadastro')
def cadastro():
    return render_template('formulario.html')
