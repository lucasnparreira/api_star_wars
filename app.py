import os
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request, send_from_directory
import requests 
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="static")

SWAPI_URL = "https://swapi.dev/api/people/"

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as f:
            f.write(response.content)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

def get_character_data(character_id):
    response = requests.get(f"{SWAPI_URL}{character_id}/")
    # response = requests.get(response)
    
    if response.status_code == 200:
        data = response.json()

        character_name = data["name"].replace(" ", "_")

        wiki_url = f"https://starwars.fandom.com/wiki/{character_name}"

        wiki_response = requests.get(wiki_url)

        if wiki_response.status_code == 200:
            soup = BeautifulSoup(wiki_response.text, 'html.parser')
            image_tag = soup.find("img", {"class":"pi-image-thumbnail"})
            if image_tag:
                image_url = image_tag["src"]
                if not image_url.startswith("https://"):
                    image_url = "https:" + image_url
                
                data["image"] = image_url

        return data
    return None

@app.route("/")
def home():
    character_ids = list(range(1,30)) 
    characters = [get_character_data(cid) for cid in character_ids]
    characters = [c for c in characters if c] 

    for character in characters:
            if 'image' in character:
                image_url = character['image']
                image_filename = secure_filename(character['name'] + '.jpg')

                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)

                if not os.path.exists(image_path):
                    download_image(image_url, image_filename)
                    print(f"Imagem baixada para: {image_path}")
                else:
                    print(f"Imagem já existe: {image_path}")

                character['image_filename'] = image_filename
            else:
                # Se não houver imagem, atribuímos um valor default
                character['image_filename'] = ''

    print(characters)
    
    return render_template("index.html", characters=characters)

@app.route("/api/character/<int:character_id>")
def api_character(character_id):
    character = get_character_data(character_id)
    if character:
        return jsonify(character)
    return jsonify({"error":"Personagem nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)