from flask import Flask, render_template
from vocabchallenge import app

@app.route('/game')
def game():
	return render_template('game.html')