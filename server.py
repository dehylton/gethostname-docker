from aiohttp import web
from socket import gethostname

async def handle(request):
    text = gethostname()
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),])

if __name__ == '__main__':
    web.run_app(app)
