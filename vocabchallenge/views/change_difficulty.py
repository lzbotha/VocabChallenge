from flask import Flask, render_template, redirect, request, flash
from vocabchallenge import app

@app.route('/change_difficulty')
def change_difficulty():
    return render_template('change_difficulty.html')