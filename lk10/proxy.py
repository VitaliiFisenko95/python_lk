"""
Что бы запустить нужно установить aiohttp, это веб фреймворк.
Тут реализован проксисервер (https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%BA%D1%81%D0%B8-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80)
Кому интересно попробуйте запустить и поклацать, мб спроксировать другой сайт. Это больше на инетрес)
"""

from aiohttp import web, client, TCPConnector

SITE_DOMAIN = 'habrahabr.ru'


async def index(request):
    path = request.path
    site_link = f'http://{SITE_DOMAIN}{path}'
    async with client.ClientSession(connector=TCPConnector(verify_ssl=False)) as sessiin:
        async with sessiin.request('GET', site_link) as remote_request:
            body = await remote_request.read()
            body = body.replace(b'https://habr.com', b'http://localhost:8232')
            response = web.Response(body=body, headers={'Content-Type': 'text/html'})
    return response


def setup_routers(app):
    app.router.add_get('/{tail:.*}', index)


async def on_startup(app):
    print('Running...')


async def on_shutdown(app):
    print('Running...')


def create_app():
    app = web.Application()
    setup_routers(app)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app


app = create_app()
web.run_app(app, port=8232, host='localhost')
