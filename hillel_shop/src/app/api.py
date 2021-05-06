import logging
import os

from flask import Flask, request, make_response

from app.errors import ErrorsMiddleware

LOG = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return {'data': 'pong'}


if __name__ == '__main__':
    LOG.info('App is starting ...')
    app.wsgi_app = ErrorsMiddleware(app.wsgi_app)
    app.run(debug=os.environ['IS_DEBUG'], host='0.0.0.0', port='80')
