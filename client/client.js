const net =  require('net');
const readline = require('readline');

// readlineインターフェースを作成
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// 質問を順番に処理する関数
const askQuestion = (query) => new Promise((resolve) => rl.question(query, resolve));

const main = async () => {
    const answer_method = await askQuestion('メソッドを入力してください: ');
    const answer_params_raw = await askQuestion('パラメータを入力してください: ');
    rl.close();

    const answer_params = answer_params_raw.split(" ").map((elm) => {
        switch (answer_method) {
            case 'floor':
            case 'nroot':
                return parseFloat(elm);
            default:
                return elm;
        }
    });
    const answer_param_types = answer_params.map((elm) => {
        return typeof elm;
    });

    const socketPath = '/tmp/unix.sock';
    const client = net.createConnection(socketPath, () => {
        client.write(JSON.stringify({
            method: answer_method,
            params: answer_params,
            param_types: answer_param_types,
            id: Date.now(),
        }));
    });

    client.on('data', (data) => {
        console.log('Received response:');
        const response = JSON.parse(data.toString());
        console.log(JSON.stringify(response, null, 4));
        client.end();
    });

    client.on('end', () => console.log('Disconnected from server'));
    client.on('error', (err) => console.error('Connection error:', err));
};

main();