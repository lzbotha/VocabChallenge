from flask import Flask, render_template
from vocabchallenge import app, database

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html',top10=database.get_top(10))