/**
 * Static site navigation and functionality
 * Handles client-side features for the deployed static site
 */

// Handle navigation for static site
document.addEventListener('DOMContentLoaded', function() {
    
    // Check if we're on a static site (GitHub Pages)
    const isStaticSite = window.location.hostname.includes('github.io') || 
                        window.location.protocol === 'file:' ||
                        !window.location.port;
    
    if (isStaticSite) {
        // Disable chatbot functionality on static site
        const chatForm = document.querySelector('.ai-input-container');
        const chatInput = document.getElementById('ai-input');
        const chatSendBtn = document.getElementById('ai-send-btn');
        
        if (chatInput && chatSendBtn) {
            chatInput.disabled = true;
            chatInput.placeholder = 'Chatbot is available in the local version only';
            chatSendBtn.disabled = true;
            chatSendBtn.textContent = 'Offline';
            
            // Add a note about the chatbot
            const messagesContainer = document.getElementById('ai-messages');
            if (messagesContainer) {
                const offlineMessage = document.createElement('div');
                offlineMessage.className = 'ai-message bot-message';
                offlineMessage.innerHTML = '<p>🤖 The AI chatbot is available when running locally. This is a static version of the portfolio deployed on GitHub Pages.</p>';
                messagesContainer.appendChild(offlineMessage);
            }
        }
        
        // Fix contact form for static site
        const contactForm = document.querySelector('.contact-form');
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                alert('Contact form submitted! Please send your message directly to venkat.chavan.n@gmail.com');
            });
        }
        
        // Show static site notice
        console.log('🌟 This is the static version of Venkat Chavan\'s portfolio deployed on GitHub Pages.');
        console.log('💻 For the full interactive experience with AI chatbot, run locally: python run.py');
    }
    
    // Enhanced navigation for mobile
    const navToggle = document.createElement('div');
    navToggle.className = 'nav-toggle';
    navToggle.innerHTML = '<i class="fas fa-bars"></i>';
    
    const navContainer = document.querySelector('.nav-container');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navContainer && navMenu) {
        navContainer.appendChild(navToggle);
        
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('nav-menu-open');
            const icon = navToggle.querySelector('i');
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        });
        
        // Close menu when clicking on a link
        navMenu.addEventListener('click', function(e) {
            if (e.target.classList.contains('nav-link')) {
                navMenu.classList.remove('nav-menu-open');
                const icon = navToggle.querySelector('i');
                icon.classList.add('fa-bars');
                icon.classList.remove('fa-times');
            }
        });
    }
});

// Smooth scrolling for anchor links (for static site)
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="./index.html#"], a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            let targetId;
            
            if (href.startsWith('./index.html#')) {
                targetId = href.substring(13); // Remove './index.html#'
            } else if (href.startsWith('#')) {
                targetId = href.substring(1); // Remove '#'
            }
            
            if (targetId && window.location.pathname.includes('index.html') || window.location.pathname === '/') {
                e.preventDefault();
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});
