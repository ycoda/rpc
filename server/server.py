import socket
import os
import json

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/unix.sock'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from {}'.format(client_address))
        data = connection.recv(2048)
        if data:
            message = data.decode('utf-8')
            json_data = json.loads(message)
            print('Receive:', json_data)

            response = json.dumps({
                "result": 19,
                "id": json_data.get("id", None)
            })
            connection.sendall(response.encode('utf-8'))
        else:
            print('no data from {}'.format(client_address))
    except json.JSONDecodeError:
        print('Invalid JSON data received: {}'.format(data))
    except Exception as e:
        print('An error occurred: {}'.format(e))
    finally:
        connection.close()
        print('removed {}'.format(client_address))
    