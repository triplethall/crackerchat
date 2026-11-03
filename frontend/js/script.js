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
    console.log("сообщение")
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// смена темы
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const currentTheme = localStorage.getItem('theme');
if (currentTheme === 'dark') {
    document.body.classList.add('dark-theme');
    themeIcon.src = 'assets/moon.svg'; // Если тема темная, показываем луну
}

// Обработчик клика по кнопке
themeToggleBtn.addEventListener('click', () => {
    // Переключаем класс dark-theme на теге body
    console.log("Кнопка нажата");
    document.body.classList.toggle('dark-theme');
    
    
    if (document.body.classList.contains('dark-theme')) {
        themeIcon.src = 'assets/moon.svg'; 
        localStorage.setItem('theme', 'dark'); 
    } else {
        themeIcon.src = 'assets/sun.svg'; 
        localStorage.setItem('theme', 'light'); 
    }
});