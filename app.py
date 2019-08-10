from flask import Flask, render_template, request
from objects.OriginalURL import OriginalURL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():

    if request.method == 'POST':
        url = OriginalURL(request.form)
        phrase = url.create_funny_phrase()

    return render_template('phrase.html', phrase=phrase)

if __name__ == "__main__":
    app.run()