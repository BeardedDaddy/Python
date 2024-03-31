const http = require('http');

const hostname = '127.0.0.1';
const port = 8080;

const msg = "Hello Team! Welcome to GCP World. I am Grevy & I hope, you are doing well."
const fulMsg = '${msg}\n';

const server = http.createServer((request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/plain');
    response.end(fulMsg);
});

server.listen(port, hostname, () => {
    console.log('Application running at http://${hostname}:${port}/');
});