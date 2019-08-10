from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<variable>')
def index(variable):
    return render_template('index.html', variable=variable)

if __name__ == "__main__":
    app.run()