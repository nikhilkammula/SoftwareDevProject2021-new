"""
Routing file that holds the information for the separate webpage links.
/index: main page for the spellchecker
"""
from app import app
from flask import render_template, request, send_from_directory
from .spell_check import *

@app.route("/translation/<path:filename>")
def lang_folder(filename):
    print(filename)
    return send_from_directory("./translation/", filename)

# Handles the about page with basic information about how to use the spell checker
@app.route('/')
@app.route('/about')
def about_page():
    return render_template("about.html")

# Handles the index page, which contains the spellchecking system 
@app.route('/index', methods=['GET', 'POST'])
def index_page():
    if request.method == "POST":
        TextToCheck = request.form.get("TextToCheck")
        TextToCheck_List = parse_txt(TextToCheck)
        results = check_word(TextToCheck_List)
        print("Input Text")
        print(TextToCheck+"\n")
        print("Incorrectly Spelled Words")
        results_words = []
        recommendations = []
        for idx in results:
            print(TextToCheck_List[idx])
            word = TextToCheck_List[idx]
            recommendations.append((word, word_candidates(word)))
            print(recommendations)
        for idx in results:
            print(TextToCheck_List[idx])
        for i in range (0, len(TextToCheck_List)):
            if i in results:
                results_words.append(('Misspelled_words', TextToCheck_List[i]))
            else:
                results_words.append(('', TextToCheck_List[i]))

        return render_template("index.html", misspelled_words=results_words, recommendations=recommendations)

    return render_template("index.html")

@app.route('/about')
def about():
    return "About"
