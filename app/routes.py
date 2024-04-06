from app import app
from flask import render_template

characters = [
    {   
        "id": 1,
        "name": "c1",
        "userid": 1
    },
    {   
        "id": 2,
        "name": "c2",
        "userid": 1
    },
    {   
        "id": 3,
        "name": "c3",
        "userid": 2
    },
]

@app.route('/')
def index():
    return render_template("index.html", title="RPG Generator")

@app.route('/characters/')
def get_characters():
    return render_template("characters.html", characters=characters, title="RPG Generator")

@app.route('/user/')
def get_user():
    return render_template("user.html", title="RPG Generator")
