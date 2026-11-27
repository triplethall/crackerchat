import { getMessages, sendMessage } from './api.js';

const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const chatMessages = document.getElementById('chat-messages');

const shownIds = new Set(); // чтобы не рисовать одно и то же дважды

function formatTime(isoDate) {
    return new Date(isoDate).toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' });
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Рисует одно сообщение
function renderMessage(message, mine = false) {
    if (shownIds.has(message.id)) return;
    shownIds.add(message.id);

    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', mine ? 'outgoing' : 'incoming');

    const p = document.createElement('p');
    p.textContent = message.text; // ВАЖНО: textContent защищает от XSS

    const time = document.createElement('span');
    time.classList = 'message-time';
    time.textContent = formatTime(message.date);

    messageDiv.append(p, time);
    chatMessages.appendChild(messageDiv);
}

// Загружает ленту
async function loadMessages() {
    const data = await getMessages();
    // Сервер отдаёт новые сверху, а нам нужно снизу, поэтому переворачиваем
    const messages = data.results.slice().reverse();
    for (const message of messages) {
        renderMessage(message);
    }
    scrollToBottom();
}

// Сервер требует поле object (тема). Берем первую строку текста.
function makeObject(text) {
    return text.split('\n')[0].slice(0, 255);
}

async function handleSend() {
    const text = messageInput.value.trim();
    if (text === '') return;

    messageInput.value = '';
    sendBtn.disabled = true; // блокируем кнопку, пока летит запрос

    try {
        const message = await sendMessage({ object: makeObject(text), text });
        renderMessage(message, true); // true = мое сообщение (справа)
        scrollToBottom();
    } catch (error) {
        console.error(error);
        messageInput.value = text; // возвращаем текст при ошибке
        alert(`Не получилось отправить.\n${error.message}`);
    } finally {
        sendBtn.disabled = false;
    }
}

// Обработчики
sendBtn.addEventListener('click', handleSend);
messageInput.addEventListener('keydown', (e) => { // keydown вместо keypress
    if (e.key === 'Enter') {
        handleSend();
    }
});

// Первая загрузка
loadMessages().catch((error) => {
    console.error(error);
    alert(`Не получилось загрузить сообщения.\n${error.message}`);
});

// --- Смена темы ----
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const currentTheme = localStorage.getItem('theme');
if (currentTheme === 'dark') {
    document.body.classList.add('dark-theme');
    themeIcon.src = 'assets/moon.svg';
}

themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    if (document.body.classList.contains('dark-theme')) {
        themeIcon.src = 'assets/moon.svg';
        localStorage.setItem('theme', 'dark');
    } else {
        themeIcon.src = 'assets/sun.svg';
        localStorage.setItem('theme', 'light');
    }
});