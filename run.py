from raven.contrib.flask import Sentry

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from vocabchallenge import config, app

if __name__ == '__main__':

    # if app.config['SENTRY_ENABLED']:
    #     sentry = Sentry(app, dsn=app.config['DATABASE_NAME'])

    app.run()
    # print 'Running in production mode'

    #figure out argparser you lazy twat

    #app.run(debug=True, host='0.0.0.0', port=args.port, use_debugger=True)
    # http_server = HTTPServer(WSGIContainer(app))
    # http_server.listen(8080, address='0.0.0.0')
    # IOLoop.instance().start()