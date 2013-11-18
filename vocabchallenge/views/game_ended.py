from flask import Flask, render_template, session
from vocabchallenge import app, database

@app.route('/game_ended', methods=('post', 'get'))
def game_ended():
    #this needs to query the database for a users past scores and shit
    highscore = database.get_highscore(123)
    database.insert_game('testee',123, session['score'],0)
    # print highscore 
    # print session['score'] 
    if session['score'] > highscore:
        print 'NEW HIGHSCORE'
    return render_template('game_ended.html', score=session['score'])