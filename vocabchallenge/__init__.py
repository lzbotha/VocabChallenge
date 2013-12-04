from flask import Flask
import vocabchallenge.config

app = Flask(__name__)
app.config.from_object('vocabchallenge.config')

from mixpanel import Mixpanel
mp = Mixpanel(config.MIXPANEL_PROJECT_TOKEN)

import vocabchallenge.database
import vocabchallenge.views