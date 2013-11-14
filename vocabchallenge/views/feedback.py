from flask import Flask, render_template, redirect, request, flash
from vocabchallenge import app

@app.route('/feedback', methods=('post', 'get'))
def feedback():
	if 'feedback' in request.form:
		feedback = request.form['feedback']
		flash('Thank you for your feedback.')
		
		# add feedback to database

		return redirect('/')
	else:
		return render_template('feedback.html')