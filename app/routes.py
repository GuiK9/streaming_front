from flask import Blueprint, render_template, request, redirect, url_for
import requests
import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
    error = None
    success = None
    videos = []

    try:
        api_url = os.getenv('DOMAIN_API') + '/api/videos'
        response = requests.get(api_url)
        error = request.args.get('error')
        success = request.args.get('success')
        videos = response.json() if response.status_code == 200 else []
    except Exception as e:
        print(f"Error fetching videos: {e}")
        videos = []
    return render_template('index.html', videos=videos, error=error, success=success)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/upload', methods=['POST'])
def upload():
    metadata_json = request.form.get('metadata')
    video_file = request.files.get('video')

    if not metadata_json or not video_file:
        return redirect(url_for('main.home', error='Metadata ou vídeo não enviados.'))

    files = {
        'metadata': (None, metadata_json, 'application/json'),
        'video': (video_file.filename, video_file.stream, video_file.mimetype)
    }

    try:
        response = requests.post(
            os.getenv('DOMAIN_API') + '/api/videos',
            files=files
        )
        if response.status_code == 201:
            return redirect(url_for('main.home', success='Vídeo enviado com sucesso!'))
        else:
            return redirect(url_for('main.home', error=f"Erro ao enviar vídeo: {response.text}"))
    except Exception as e:
        return redirect(url_for('main.home', error=f"Erro ao conectar à API: {e}"))

@main.route('/cadastro')
def cadastro():
    domain_api = os.getenv('DOMAIN_API')
    return render_template('formulario.html', domain_api=domain_api)