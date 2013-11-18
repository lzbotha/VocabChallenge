from flask import Flask, render_template, session, flash
from vocabchallenge import app, database

@app.route('/game_ended', methods=('post', 'get'))
def game_ended():
    #this needs to query the database for a users past scores and shit
    highscore = database.get_highscore(session['userid'])
    database.insert_game(session['userid'], session['score'])
    if session['score'] > highscore:
        flash('NEW HIGHSCORE')
    return render_template('game_ended.html', score=session['score'])