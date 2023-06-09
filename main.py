import asyncio
import websockets
from flask import Flask, request
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)
connected = set()

async def handle_chat(websocket, path):
    connected.add(websocket)

    try:
        welcome_message = "Welcome to the chat! Please enter your name: "
        await websocket.send(welcome_message)

        client_name = await websocket.recv()
        message = f"{client_name} entered the chat."
        await broadcast(message)

        while True:
            try:
                client_message = await websocket.recv()
                complete_message = f"{client_name}: {client_message}"
                await broadcast(complete_message)

            except websockets.ConnectionClosed:
                connected.remove(websocket)
                message = f"{client_name} leave the chat."
                await broadcast(message)
                break

    except Exception as e:
        print(f"Error: {e}")

async def broadcast(message):
    if connected:
        await asyncio.wait([ws.send(message) for ws in connected])

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return 'Endpoint'

    elif request.method == 'POST':
        if 'message' in request.form:
            message = request.form['message']
            asyncio.run(broadcast(message))
            return 'Message sent'

    return 'unsupported method'

@sockets.route('/ws')
def websocket_route(ws):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(handle_chat(ws, ''))

if __name__ == '__main__':
    app.run()
