from flask import Flask, render_template, redirect, request, session, flash
from vocabchallenge import app, database, mp
import random

@app.route('/game/<lang>', methods=('post', 'get'))
def game(lang):

    #if the player is currently in a game
    if session.pop('ingame',False):

        #word and definition retrieved from database
        if 'wordnum' in session:

            #user has submitted feedback
            if 'wordguess' in request.form:
                try:
                    wordguess = int(request.form['wordguess']) - 1
                except ValueError:
                    wordguess = -1

                #user has guessed the word correctly
                if wordguess == session.pop('wordnum'):
                    flash('Correct!')
                    session['ingame'] = True
                    session['score'] += 1
                    return redirect('/game/'+lang)

                #user has incorrectly guessed the word
                else:
                    session['lives'] -= 1

                    #tell the user if they are entering the wrong input
                    if 0<=wordguess<=3:
                        flash('Incorrect, the correct answer was: '+session['word'])
                    else:
                        flash('Please only enter numbers between 1-4')
                    #player has no guesses remaining
                    if session['lives'] < 1:
                        return redirect('/game_ended')
                    session['ingame'] = True
                    return redirect('/game/'+lang)

            #user has not yet submitted feedback
            else:
                session['ingame'] = True
                return render_template('game.html', words=session['words'], definition=session['definition'], lang=lang, lives=session['lives'], score=session['score'])
        
        #word and definition not yet retrieved from database
        else:
            session['ingame'] = True
            session['word'], session['definition'] = database.get_entry(lang)
            session['words'] = database.get_padding_words(lang, session['word'] ,3)

            session['wordnum'] = int(round(random.uniform(0,3)))

            session['words'].insert(session['wordnum'] ,session['word'])
            return render_template('game.html', words=session['words'], definition=session['definition'], lang=lang, lives=session['lives'], score=session['score'])

    #if the player is not yet in a game initialize variables for a new game
    else:
        #note that this value is set to true before the user is redirected to /game. This is so that the game is ended if the user quits the game (consider implementing this in a better way)
        session['ingame'] = True
        session['language'] = lang
        session['score'] = 0
        session['lives'] = 3
        #so each new quiz starts with a new word
        session.pop('word', None)
        session.pop('wordnum', None)
        mp.track(session['username'],'new game: '+lang)
        return redirect('/game/'+lang)