from flask import Flask, render_template
from vocabchallenge import app

@app.route('/game_ended')
def game_ended():
    #this needs to query the database for a users past scores and shit
    return render_template('game_ended.html')