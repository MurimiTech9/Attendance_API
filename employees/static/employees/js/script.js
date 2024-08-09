// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Add a class to highlight the current page in the navigation
    const currentPage = window.location.pathname;
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });

    // Example function to show a welcome message
    function showWelcomeMessage() {
        const main = document.querySelector('main');
        const welcomeMessage = document.createElement('div');
        welcomeMessage.textContent = 'Welcome to the Attendance API!';
        welcomeMessage.style.padding = '10px';
        welcomeMessage.style.backgroundColor = '#f0f0f0';
        welcomeMessage.style.marginBottom = '20px';
        main.insertBefore(welcomeMessage, main.firstChild);
    }

    // Call the welcome message function
    showWelcomeMessage();

    // You can add more JavaScript functionality here as needed
});
