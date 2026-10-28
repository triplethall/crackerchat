const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const chatMessages = document.getElementById('chat-messages');

// Функция отправки сообщения
function sendMessage() {
    const text = messageInput.value.trim();
    
    // Если поле пустое, ничего не делаем
    if (text === '') return;

    // Создаем новый элемент сообщения
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'outgoing'); // Добавляем классы
    
    const p = document.createElement('p');
    p.textContent = text;
    
    messageDiv.appendChild(p);
    chatMessages.appendChild(messageDiv);

    messageInput.value = '';

    // Автоскролл вниз к последнему сообщению
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Вешаем обработчик события на кнопку
sendBtn.addEventListener('click', sendMessage);

// Вешаем обработчик на нажатие клавиши Enter 
messageInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});