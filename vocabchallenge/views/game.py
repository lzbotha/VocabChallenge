from flask import Flask, render_template, redirect, request, session
from vocabchallenge import app, database

@app.route('/game', methods=('post', 'get'))
def game():
    
    if session.pop('ingame',False):

        #word and definition retrieved from database
        if 'word' in session:

            #user has submitted feedback
            if 'wordguess' in request.form:
                wordguess = request.form['wordguess']

                #user has guessed the word correctly
                if wordguess == session.pop('word'):
                    session['ingame'] = True
                    session['score'] += 1
                    return redirect('/game')

                #user has incorrectly guessed the word
                else:
                    if session['lives'] > 0:
                        session['lives'] -= 1
                        session['ingame'] = True
                        return redirect('/game')
                    return redirect('/game_ended')

            #user has not yet submitted feedback
            else:
                session['ingame'] = True
                return render_template('game.html', word=session['word'], definition=session['definition'])
        
        #word and definition not yet retrieved from database
        else:
            session['ingame'] = True
            session['word'], session['definition'] = database.get_entry(0)
            return render_template('game.html', word=session['word'], definition=session['definition'])

    else:
        session['ingame'] = True
        session['score'] = 0
        session['lives'] = 3
        return redirect('/game')