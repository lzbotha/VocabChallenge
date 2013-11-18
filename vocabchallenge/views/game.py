from flask import Flask, render_template, redirect, request, session
from vocabchallenge import app, database

@app.route('/game', methods=('post', 'get'))
def game():
    
    #if the player is currently in a game
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
                    session['lives'] -= 1

                    #player has no guesses remaining
                    if session['lives'] < 1:
                        return redirect('/game_ended')
                        
                    session['ingame'] = True
                    return redirect('/game')

            #user has not yet submitted feedback
            else:
                session['ingame'] = True
                return render_template('game.html', word=session['word'], definition=session['definition'])
        
        #word and definition not yet retrieved from database
        else:
            session['ingame'] = True
            session['word'], session['definition'] = database.get_entry(0)
            return render_template('game.html', word=session['word'], definition=session['definition'])

    #if the player is not yet in a game initialize variables for a new game
    else:
        #note that this value is set to true before the user is redirected to /game. This is so that the game is ended if the user quits the game (consider implementing this in a better way)
        session['ingame'] = True
        session['score'] = 0
        session['lives'] = 3
        return redirect('/game')