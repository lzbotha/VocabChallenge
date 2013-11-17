from flask import Flask, render_template, redirect, request, session
from vocabchallenge import app, database


# def game():
#     # if the game is lost it needs to redirect to game_ended
#     if True:
#         word, definition = database.get_entry(0)
#         if 'wordguess' in request.form:
#             wordguess = request.form['wordguess']

#             # player guessed the word right
#             if wordguess == word:
#                 # could prob stick the users current score is session
#                 print 'well done'
#             return redirect('/game')
#         else:
#             return render_template('game.html', word=word, definition=definition)
#     else:
#         redirect('/game_ended')

#session['logged_in'] = True
@app.route('/game', methods=('post', 'get'))
def game():
    print 'word' in session
    if 'word' in session:

        #user has submitted feedback
        if 'wordguess' in request.form:
            wordguess = request.form['wordguess']

            #user has guessed the word correctly
            if wordguess == session.pop('word'):
                return redirect('/game')

            #user has incorrectly guessed the word
            else:
                return redirect('/game_ended')

        #user has not yet submitted feedback
        else:
            return render_template('game.html', word=session['word'], definition=session['definition'])
    else:
        session['word'], session['definition'] = database.get_entry(0)
        print (session['word'], session['definition'])
        return render_template('game.html', word=session['word'], definition=session['definition'])