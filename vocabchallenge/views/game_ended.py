from flask import Flask, render_template, session, flash
from vocabchallenge import app, database, mp

@app.route('/game_ended', methods=('post', 'get'))
def game_ended():
    mp.track(session['username'],'game ended: '+ session['language'])

    highscore = database.get_highscore(session['userid'])
    database.insert_score(session['userid'], session['language'] ,session['score'])
    if session['score'] > highscore:
        flash('NEW HIGHSCORE')
    return render_template('game_ended.html', score=session['score'])