from flask import Flask, render_template, session
from vocabchallenge import app, database

@app.route('/leaderboard')
def leaderboard():
    session.pop('ingame',None)
    return render_template('leaderboard.html',top10=database.get_top(10))