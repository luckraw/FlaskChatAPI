# Sobre o projeto

FlaskChatAPI é um projeto de API de chat em tempo real construído com o framework Flask e websockets. Ele permite que os usuários se conectem e troquem mensagens em um ambiente de chat interativo.

## Tecnologias utilizadas

- Python
- Flask
- Flask-Sockets
- Websockets

## Instalação

Clone este repositório:

```shell
git clone https://github.com/luckraw/FlaskChatAPI.git
```
Acesse o diretório do projeto:
```
cd FlaskChatAPI
```
Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
source venv/bin/activate
```
## Como usar

Inicie o servidor da API Flask:
```
python main.py
```
Acesse a API em http://localhost:5000.

Use o endpoint /chat para enviar mensagens por meio de solicitações POST. Exemplo:
```
curl -X POST -d "message=Olá, mundo!" http://localhost:5000/chat
```
Para interagir em tempo real com o chat, estabeleça uma conexão websocket usando o endpoint /ws. Exemplo em JavaScript:
```javascript
const socket = new WebSocket('ws://localhost:5000/ws');

socket.onopen = () => {
  console.log('Conexão estabelecida');
};

socket.onmessage = (event) => {
  const message = event.data;
  console.log('Mensagem recebida:', message);
};

socket.onclose = () => {
  console.log('Conexão encerrada');
};

// Enviar mensagem para o chat
socket.send('Olá, mundo!');
```

