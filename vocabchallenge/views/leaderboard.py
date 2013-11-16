from flask import Flask, render_template
from vocabchallenge import app

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')