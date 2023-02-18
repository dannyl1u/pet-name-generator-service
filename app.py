import os
import random

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

import random

def add_french_accents(word):
    """
    Adds random French accents to a word
    """
    accents = ['é', 'è', 'ê', 'ë', 'à', 'â', 'î', 'ï', 'ô', 'ù', 'û']
    accented_word = ''
    for letter in word:
        accented_word += letter + random.choice(accents)
    return accented_word

def add_french_verbs(word):
    """
    Adds random French verbs to a word
    """
    verbs = ['aller', 'avoir', 'être', 'faire', 'pouvoir', 'savoir', 'vouloir']
    verb = random.choice(verbs)
    verb_word = f'{verb} {word}'
    return verb_word

def translate_to_french(text):
    """
    Translates an English string to French
    """
    words = text.split()
    translated_words = []
    for word in words:
        accented_word = add_french_accents(word)
        # verb_word = add_french_verbs(accented_word)
        # translated_words.append(verb_word)
        translated_words.append(accented_word)
    translated_text = ' '.join(translated_words)
    return translated_text


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=translate_to_french(response.choices[0].text.split()[0])))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
