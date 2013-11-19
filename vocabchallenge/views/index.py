from flask import Flask, render_template, session
from vocabchallenge import app

@app.route('/')
def index():
    session.pop('ingame', None)
    return render_template('index.html',username=session['username'])