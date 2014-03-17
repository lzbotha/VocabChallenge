from flask import Flask
import vocabchallenge.config
import urllib
from markupsafe import Markup

app = Flask(__name__)
app.config.from_object('vocabchallenge.config')

@app.template_filter('urlencode')
def urlencode_filter(s):
    if type(s) == 'Markup':
        s = s.unescape()
    s = s.encode('utf8')
    s = urllib.quote_plus(s)
    return Markup(s)

from mixpanel import Mixpanel
mp = Mixpanel(config.MIXPANEL_PROJECT_TOKEN)

import vocabchallenge.database
import vocabchallenge.views