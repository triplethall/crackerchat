import { MESSAGES_URL } from './config.js';

async function request(url, options = {}) {
    const response = await fetch(url, options);
    if (!response.ok) {
        const body = await response.json().catch(() => null);
        throw new Error(`Сервер ответил ${response.status}${body ? ': ' + JSON.stringify(body) : ''}`);
    }
    return response.json();
}

// GET: загрузка сообщений
export async function getMessages(url = MESSAGES_URL) {
    console.log("get_messages");
    return request(url);
}

// POST: отправка сообщения
export async function sendMessage({ object, text }) {
    return request(MESSAGES_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ object, text }),
    });
}