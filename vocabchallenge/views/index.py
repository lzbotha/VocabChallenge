from flask import Flask, render_template, session
from vocabchallenge import app, mp

@app.route('/')
def index():
    session.pop('ingame', None)
    mp.track(session['username'],'index viewed')
    return render_template('index.html',username=session['username'])