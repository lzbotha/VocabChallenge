from flask import Flask, render_template
from vocabchallenge import app

@app.route('/feedback')
def feedback():
	return render_template('feedback.html')