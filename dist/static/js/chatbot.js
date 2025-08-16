document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chatMessages');
    const chatInput = document.getElementById('chatInput');
    const sendButton = document.getElementById('sendButton');
    const typingIndicator = document.getElementById('typingIndicator');
    const suggestionButtons = document.querySelectorAll('.suggestion-btn');

    // Event listener for send button
    sendButton.addEventListener('click', sendMessage);

    // Event listener for Enter key in input field
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Event listeners for suggestion buttons
    suggestionButtons.forEach(button => {
        button.addEventListener('click', () => {
            chatInput.value = button.textContent;
            sendMessage();
        });
    });

    function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        addMessage(message, 'user');
        chatInput.value = '';
        showTyping();

        // Send message to the backend API
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            hideTyping();
            if (data.response) {
                addMessage(data.response, 'bot');
            } else {
                addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        })
        .catch(error => {
            hideTyping();
            console.error('Error:', error);
            addMessage('Sorry, I encountered a connection error. Please check the server.', 'bot');
        });
    }

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = sender === 'user' ? '<i class="fas fa-user-astronaut"></i>' : '<i class="fas fa-robot"></i>';

        const content = document.createElement('div');
        content.className = 'message-content';
        
        // Sanitize and format the text
        const formattedText = text.replace(/\n/g, '<br>');
        content.innerHTML = `<p>${formattedText}</p>`;

        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function showTyping() {
        typingIndicator.style.display = 'flex';
        sendButton.disabled = true;
        chatInput.disabled = true;
    }

    function hideTyping() {
        typingIndicator.style.display = 'none';
        sendButton.disabled = false;
        chatInput.disabled = false;
        chatInput.focus();
    }
});
