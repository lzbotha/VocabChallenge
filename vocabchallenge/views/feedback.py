from flask import Flask, render_template, redirect, request, flash, session
from vocabchallenge import app, database

@app.route('/feedback', methods=('post', 'get'))
def feedback():
    session.pop('ingame', None)
    if 'feedback' in request.form:
        feedback = request.form['feedback']
        database.feedback(session['userid'], feedback)
        flash('Thank you for your feedback.')
        

        return redirect('/')
    else:
        return render_template('feedback.html')