from flask import Flask
import vocabchallenge.config

app = Flask(__name__)
app.config.from_object('vocabchallenge.config')

import vocabchallenge.database
import vocabchallenge.views