from flask import Flask, render_template, request, redirect, url_for
from objects.OriginalURL import OriginalURL
from objects.GeneratedPhrase import Phrase

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():

    if request.method == 'POST':
        url = OriginalURL(request.form['url'])
        phrase = url.create_funny_phrase()
        db_count = url.does_url_already_exist()
        db_write = url.write_generated_phrase_to_db()

    return render_template('phrase.html', phrase=phrase)

@app.route('/route_to/<phrase>')
def route_to(phrase):
    phrase_object = Phrase(phrase)
    redirect_url = phrase_object.get_url()
    return redirect(redirect_url)

if __name__ == "__main__":
    app.run()