from flask import Flask, render_template, session
from vocabchallenge import app, database

@app.route('/leaderboard/')
@app.route('/leaderboard/<language>')
def leaderboard(language=None):
    session.pop('ingame',None)
    if language:
        return render_template('leaderboard.html',top10=database.get_top_by_language(10,language))
    else:
        return render_template('leaderboard.html',top10=database.get_top(10))