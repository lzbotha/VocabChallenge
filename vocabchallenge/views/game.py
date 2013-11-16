from flask import Flask, render_template, redirect, request, session
from vocabchallenge import app, database

@app.route('/game', methods=('post', 'get'))
def game():
    # if the game is lost it needs to redirect to game_ended
    if True:
        word, definition = database.get_entry(0)
        if 'wordguess' in request.form:
            wordguess = request.form['wordguess']

            # player guessed the word right
            if wordguess == word:
                # could prob stick the users current score is session
                print 'well done'
            return redirect('/game')
        else:
            return render_template('game.html', word=word, definition=definition)
    else:
        redirect('/game_ended')

#session['logged_in'] = True