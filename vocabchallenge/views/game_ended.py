from flask import Flask, render_template
from vocabchallenge import app

@app.route('/game_ended')
def game_ended():
	return render_template('game_ended.html')