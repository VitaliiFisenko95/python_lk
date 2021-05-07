import logging
import os

from flask import Flask, request, make_response

from app.errors import ErrorsMiddleware
from app.db import db
from app import controllers as c

LOG = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/api/ping', methods=['GET'])
def ping():
    return {'data': 'pong'}


@app.route('/internal-api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    with db() as conn:
        product = c.create_product(conn, data)
        if not product:
            return make_response({}, 500)
    return make_response({'data': product[0]}, 200)


if __name__ == '__main__':
    LOG.info('App is starting ...')
    # app.wsgi_app = ErrorsMiddleware(app.wsgi_app)
    app.run(debug=os.environ['IS_DEBUG'], host='0.0.0.0', port='80')
