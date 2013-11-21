from flask import Flask, render_template
from vocabchallenge import app, database

@app.route('/profile/<username>')
def profile(username):
    userid = database.get_userid(username)
    games_played = database.get_num_games(userid)
    highscore = database.get_highscore(userid)
    return render_template('profile.html', 
                            username=username,
                            games_played=games_played,
                            highscore=highscore)