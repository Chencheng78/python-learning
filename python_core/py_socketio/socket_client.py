import time

import socketio
import asyncio

BASE_URL = 'http://127.0.0.1:8080'
ws = socketio.AsyncClient()
start_timer = None


async def send_ping():
    global start_timer
    start_timer = time.time()
    await ws.emit('heartbeat', 'send heartbeat')

@ws.on('SendtoClient')
def on_message(data: str) -> None:
    print('message received')
    print(data)


@ws.event
def disconnect() -> None:
    print("I'm disconnected!")


@ws.event
async def connect() -> None:
    print("I'm connected!")
    await send_ping()


# @ws.event()
@ws.on('heartbeat')
async def pong_from_server():
    global start_timer
    latency = time.time() - start_timer
    print(f'current_time: {time.strftime("%D-%H:%M:%S")}latency is {latency * 1000:.2f} ms')
    if latency > 2:
        await ws.disconnect()
    await ws.sleep(1)
    if ws.connected:
        await send_ping()


# print('current sid: ', ws.sid)
# n = 0
# while n < 20:
#     ws.on('SendtoClient', on_message)
#     # await ws.emit('message', 'hello world')
#     await asyncio.sleep(1)
#     n += 1

# await ws.disconnect()

async def main() -> None:
    await ws.connect(BASE_URL)
    await ws.wait()

if __name__ == "__main__":
    asyncio.run(main())
