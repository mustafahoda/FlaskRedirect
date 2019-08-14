# FlaskRedirect

FlaskRedirect is a FlaskApp that does a very simple job. You enter a url and the FlaskApp generates a funny phrase.
Once the FlaskApp is running, you can then go to 'localhost:<port_number>/route_to/<funny_phrase>' and the app will
redirect to the original url.

## Motivation

The motivation behind this app was to build a simple Flask App that will help me better undestand the fundamentals
of FlaskApps such as routing. In doing so, I was also able to play with the PyMongo Package.


## How it works

The FlaskApp takes in the original URL and using the RandomWords Python Package, generates a 3 worded funny phrase.
The funny phrase and it's corresponding URL is written to a MongoDB Database running locally.


## Installation

**You need to have MongoDB installed on your machine to keep track of url and their phrases.**

pipenv will install all required dependencies onto your machine

```bash
pipenv install
```

## Usage

```python
python app.py
```

- Once your app is running, navigate to where the server is running. Usually this is `localhost:5000`.
- Enter the URL for one of your favorite websites into the text box and click "Make me funny".
- You'll be directed to a new page `localhost:5000/generate` that will display the phrase.
- Copy that phrase
- Now go to: `localhost:5000/route_to/<funny_phrase>`
- The FlaskApp will redirect to the original URL you had entered.