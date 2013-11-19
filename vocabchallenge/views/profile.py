from flask import Flask, render_template
from vocabchallenge import app

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username)