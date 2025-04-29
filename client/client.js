const net =  require('net');

const socketPath = '/tmp/unix.sock';
const client = net.createConnection(socketPath, () => {
    client.write(JSON.stringify({
        method: "subtract",
        params: [42, 23],
        param_types: ["int", "int"],
        id: 1
    }));
});

client.on('data', (data) => {
    console.log('Received from server:', data.toString());
    client.end();
});

client.on('end', () => {
    console.log('Disconnected from server');
});

client.on('error', (err) => {
    console.error('Connection error:', err);
});