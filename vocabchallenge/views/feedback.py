from flask import Flask, render_template, redirect, request, flash
from vocabchallenge import app, database

@app.route('/feedback', methods=('post', 'get'))
def feedback():
	if 'feedback' in request.form:
		feedback = request.form['feedback']
		database.feedback('testee', '123', feedback)
		flash('Thank you for your feedback.')
		

		return redirect('/')
	else:
		return render_template('feedback.html')