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
    # accents = ['é', 'è', 'ê', 'ë', 'à', 'â', 'î', 'ï', 'ô', 'ù', 'û']
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_dict = {
        "a": ['à', 'â'],
        "e": ['é', 'è', 'ê', 'ë'],
        "i": ['î', 'ï'],
        "o": ['ô'],
        "u": ['ù', 'û']
    }

    accented_word = ''
    for letter in word:
        if letter in vowels:
            letter = random.choice(vowel_dict[letter])
            accented_word += letter
        else:
            accented_word += letter
    if (accented_word[len(accented_word) - 1] == 'n'):
        accented_word += 'é'
    return accented_word

def translate_to_french(text):
    """
    Translates an English string to French
    """
    words = text.split()
    translated_words = []
    for word in words:
        accented_word = add_french_accents(word)
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
        return redirect(url_for("index", result=translate_to_french(response.choices[0].text)))

    result = request.args.get("result")
    # return result
    return render_template("index.html", result=result)



def generate_prompt(animal):
    return """Suggest one funny animal name that is also a pun.

Animal: Cat
Names: Clawdia
Animal: Dog
Names: Chewbarka
Animal: {}
Names:""".format(
        animal.capitalize()
    )
