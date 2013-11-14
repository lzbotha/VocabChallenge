from flask import Flask

app = Flask(__name__)

import vocabchallenge.database
import vocabchallenge.views