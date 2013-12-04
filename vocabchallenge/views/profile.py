from flask import Flask, render_template
from vocabchallenge import app, database, mp

@app.route('/profile/<username>')
def profile(username):
    mp.track(session['username'],'profile viewed')
    userid = database.get_userid(username)
    games_played = database.get_num_games(userid)
    highscore = database.get_highscore(userid)
    breakdown = database.get_breakdown(userid)
    return render_template('profile.html', 
                            username=username,
                            games_played=games_played,
                            highscore=highscore,
                            breakdown=breakdown)