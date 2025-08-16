/**
 * Static Site JavaScript - Handles client-side functionality for GitHub Pages deployment
 * Replaces server-side Flask functionality with client-side solutions
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // Mobile navigation toggle
    initMobileNavigation();
    
    // Smooth scrolling for anchor links
    initSmoothScrolling();
    
    // Project cards interactions
    initProjectCards();
    
    // Navigation highlighting
    initNavigationHighlighting();
    
    // Chatbot functionality (static version)
    if (window.location.pathname.includes('chatbot.html')) {
        initStaticChatbot();
    }
    
    console.log('Static site JavaScript initialized');
});

/**
 * Initialize mobile navigation functionality
 */
function initMobileNavigation() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
        
        // Close menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            });
        });
    }
}

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href*="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Check if it's a same-page anchor link
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
            // Handle cross-page anchor links
            else if (href.includes('#')) {
                const [page, anchor] = href.split('#');
                if (page === './index.html' || page === 'index.html') {
                    // Store the anchor for after page load
                    sessionStorage.setItem('scrollToAnchor', anchor);
                }
            }
        });
    });
    
    // Check for stored anchor on page load
    const storedAnchor = sessionStorage.getItem('scrollToAnchor');
    if (storedAnchor) {
        sessionStorage.removeItem('scrollToAnchor');
        setTimeout(() => {
            const targetElement = document.getElementById(storedAnchor);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }, 100);
    }
}

/**
 * Initialize project card interactions
 */
function initProjectCards() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        // Add hover effects
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        // Handle "Learn More" button clicks
        const learnMoreBtn = card.querySelector('.btn-primary, .learn-more-btn');
        if (learnMoreBtn) {
            learnMoreBtn.addEventListener('click', function(e) {
                // Let the default link behavior work
                console.log('Navigating to project details...');
            });
        }
    });
}

/**
 * Initialize navigation highlighting based on current page
 */
function initNavigationHighlighting() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-menu a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        
        // Remove active class from all links first
        link.classList.remove('active');
        
        // Add active class to current page link
        if ((currentPage === 'index.html' && (href === './index.html' || href === '/' || href === '#home')) ||
            (currentPage === 'chatbot.html' && href === './chatbot.html') ||
            (currentPage === 'narrative_nexus.html' && href === './narrative_nexus.html')) {
            link.classList.add('active');
        }
    });
}

/**
 * Initialize static chatbot functionality
 */
function initStaticChatbot() {
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-button');
    
    if (!chatMessages || !chatInput || !sendButton) return;
    
    // Add initial bot message
    addBotMessage("Hello! I'm a static version of the portfolio chatbot. While I can't connect to AI services in this demo, I can share some information about this portfolio!");
    
    // Handle send button click
    sendButton.addEventListener('click', sendStaticMessage);
    
    // Handle enter key in input
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendStaticMessage();
        }
    });
    
    function sendStaticMessage() {
        const message = chatInput.value.trim();
        if (!message) return;
        
        // Add user message
        addUserMessage(message);
        chatInput.value = '';
        
        // Generate static bot response
        setTimeout(() => {
            const response = generateStaticResponse(message);
            addBotMessage(response);
        }, 1000);
    }
    
    function addUserMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message user-message';
        messageDiv.innerHTML = `
            <div class="message-content">
                <p>${escapeHtml(message)}</p>
            </div>
        `;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function addBotMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot-message';
        messageDiv.innerHTML = `
            <div class="message-content">
                <p>${message}</p>
            </div>
        `;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function generateStaticResponse(userMessage) {
        const message = userMessage.toLowerCase();
        
        if (message.includes('project') || message.includes('work')) {
            return "I've worked on various exciting projects including AI/ML applications, web development, and data analysis. You can explore them in the Projects section of the portfolio!";
        } else if (message.includes('skill') || message.includes('technology')) {
            return "My skills include Python, JavaScript, React, Flask, Machine Learning, Data Science, and more. Check out the Skills section on the main page for a complete list!";
        } else if (message.includes('experience') || message.includes('background')) {
            return "I have experience in software development, data science, and AI/ML. Visit the Experience section on the homepage to learn more about my professional journey!";
        } else if (message.includes('education') || message.includes('study')) {
            return "My educational background includes studies in Computer Science and related fields. You can find more details in the Education section of the portfolio!";
        } else if (message.includes('contact') || message.includes('reach')) {
            return "You can reach out to me through the contact information provided in the portfolio. I'm always open to discussing new opportunities and collaborations!";
        } else if (message.includes('hello') || message.includes('hi') || message.includes('hey')) {
            return "Hello there! I'm excited to help you learn more about this portfolio. Feel free to ask about projects, skills, experience, or anything else you'd like to know!";
        } else {
            return "Thanks for your interest! This is a static demo of the chatbot. For a full interactive experience with AI-powered responses, please check out the live version of the portfolio. Feel free to explore the other sections to learn more!";
        }
    }
    
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

/**
 * Utility function to show loading states
 */
function showLoading(element) {
    if (element) {
        element.innerHTML = '<div class="loading">Loading...</div>';
    }
}

/**
 * Utility function to handle errors gracefully
 */
function handleError(error, fallbackMessage = 'Something went wrong. Please try again.') {
    console.error('Static site error:', error);
    return fallbackMessage;
}

// Export functions for global access if needed
window.StaticSite = {
    initMobileNavigation,
    initSmoothScrolling,
    initProjectCards,
    initNavigationHighlighting
};
