const chatWindow = document.getElementById('chatWindow');
const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');

function addMessage(content, role) {
    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${role}`;
    bubble.textContent = content;
    chatWindow.appendChild(bubble);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage(message) {
    addMessage(message, 'user');

    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    addMessage(data.reply, 'bot');
}

chatForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const message = messageInput.value.trim();
    if (!message) {
        return;
    }

    messageInput.value = '';
    messageInput.focus();
    await sendMessage(message);
});

// Initial greeting
addMessage('Hello! I am Open Road AI. I currently understand these prompts:\ndetails about <road-name>\nreport a pothole in <road-name>', 'bot');
