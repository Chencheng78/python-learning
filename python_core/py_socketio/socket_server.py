import asyncio

from aiohttp import web
import socketio
import time

sio = socketio.AsyncServer()

app = web.Application()

sio.attach(app)


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')



@sio.on('message')
async def print_message(sid, message):
    print('Socket ID: ', sid)
    print(message)
    await sio.emit('SendtoClient', time.strftime('%D-%H:%M:%S'))


@sio.on('heartbeat')
async def heartbeat_server(sid, message):
    print('Socket ID: ', sid)
    print(message)
    await asyncio.sleep(2)
    await sio.emit('heartbeat')

app.router.add_get('/', index)

if __name__ == "__main__":
    web.run_app(app)
