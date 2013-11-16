from flask import Flask, render_template
from vocabchallenge import app

@app.route('/profile')
def profile():
    return render_template('profile.html')