import logging

from flask import Response

LOG = logging.getLogger(__name__)
ERROR_DICT = {}


class ErrorsMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except tuple(ERROR_DICT) as ex:
            code, message = ERROR_DICT[type(ex)]
            LOG.info(message.format(ex))
            res = Response(message.format(ex), mimetype='application/json', status=code)
            return res(environ, start_response)
        except Exception as ex:
            LOG.exception(f'Unknown error caught in API - {ex}')
            res = Response('Internal server error', mimetype='application/json', status=500)
            return res(environ, start_response)
