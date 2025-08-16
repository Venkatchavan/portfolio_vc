// Narrative Nexus specific javascript
//----------------------------------------------------------------

// Particles.js Configuration for Narrative Nexus
particlesJS("particles-js", {
    "particles": {
      "number": {
        "value": 50,
        "density": {
          "enable": true,
          "value_area": 800
        }
      },
      "color": {
        "value": ["#00aaff", "#00ff7f", "#c0c0c0"]
      },
      "shape": {
        "type": "edge",
        "stroke": {
          "width": 0,
          "color": "#000000"
        },
      },
      "opacity": {
        "value": 0.6,
        "random": true,
      },
      "size": {
        "value": 4,
        "random": true,
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#c0c0c0",
        "opacity": 0.3,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 3,
        "direction": "none",
        "random": true,
        "straight": false,
        "out_mode": "out",
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": true,
          "mode": "bubble"
        },
        "onclick": {
          "enable": true,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "bubble": {
          "distance": 250,
          "size": 8,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "push": {
          "particles_nb": 4
        }
      }
    },
    "retina_detect": true
  });
  
  // Modal Handling for Poems
  const modal = document.getElementById('poemModal');
  const modalTitle = document.getElementById('modalPoemTitle');
  const modalContent = document.getElementById('modalPoemContent');
  const closeBtn = document.querySelector('.close-btn');
  
  const openModal = (title, content) => {
      modalTitle.textContent = title;
      modalContent.innerHTML = content.replace(/\n/g, '<br>');
      modal.style.display = 'block';
  };
  
  const closeModal = () => {
      modal.style.display = 'none';
  };
  
  // Blog Modal Handling
  const blogModal = document.getElementById('blogModal');
  const blogModalTitle = document.getElementById('modalBlogTitle');
  const blogModalContent = document.getElementById('modalBlogContent');
  const blogCloseBtn = document.querySelector('.blog-close-btn');
  
  const openBlogModal = (title, content) => {
      blogModalTitle.textContent = title;
      blogModalContent.innerHTML = content.replace(/\n/g, '<br>');
      blogModal.style.display = 'block';
  };
  
  const closeBlogModal = () => {
      blogModal.style.display = 'none';
  };
  
  // Event Listeners for Poems
  document.querySelectorAll('.read-poem-btn').forEach(button => {
      button.addEventListener('click', () => {
          const title = button.dataset.poemTitle;
          const content = button.dataset.poemContent;
          openModal(title, content);
      });
  });
  
  // Event Listeners for Blogs
  document.querySelectorAll('.read-blog-btn').forEach(button => {
      button.addEventListener('click', () => {
          const title = button.dataset.blogTitle;
          const content = button.dataset.blogContent;
          openBlogModal(title, content);
      });
  });
  
  closeBtn.addEventListener('click', closeModal);
  blogCloseBtn.addEventListener('click', closeBlogModal);
  
  window.addEventListener('click', (event) => {
      if (event.target == modal) {
          closeModal();
      }
      if (event.target == blogModal) {
          closeBlogModal();
      }
  });
  
  // AI Chat
  const aiInput = document.getElementById('ai-input');
  const aiSendBtn = document.getElementById('ai-send-btn');
  const aiMessages = document.getElementById('ai-messages');
  
  const addMessage = (message, sender) => {
      const messageEl = document.createElement('div');
      messageEl.classList.add('ai-message', `${sender}-message`);
      messageEl.innerHTML = `<p>${message}</p>`;
      aiMessages.appendChild(messageEl);
      aiMessages.scrollTop = aiMessages.scrollHeight;
  };
  
  const handleAIChat = async () => {
      const message = aiInput.value.trim();
      if (!message) return;
  
      addMessage(message, 'user');
      aiInput.value = '';
      aiSendBtn.disabled = true;
  
      try {
          const response = await fetch('/api/chat', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ message }),
          });
          const data = await response.json();
          addMessage(data.response, 'bot');
      } catch (error) {
          addMessage('Error connecting to the AI. Please try again.', 'bot');
      } finally {
          aiSendBtn.disabled = false;
      }
  };
  
  aiSendBtn.addEventListener('click', handleAIChat);
  aiInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
          handleAIChat();
      }
  });
  