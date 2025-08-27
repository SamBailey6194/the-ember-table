/**
 * Navbar interactions:
 * - Toggles mobile menu visibility.
 * - Handles logout confirmation modal.
 */
const burgerBtn = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');
const logoutModal = document.getElementById('logout-modal');
const openLogoutBtns = document.querySelectorAll('[data-open-logout]');
const closeLogoutBtn = document.getElementById('close-logout');

// Toggle mobile menu on burger click
burgerBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Open logout confirmation modal
openLogoutBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        if (logoutModal.showModal) {
            logoutModal.showModal();
        } else {
            alert("The dialog API is not supported in this browser.");
        }
    });
});

// Close logout modal
closeLogoutBtn.addEventListener('click', () => {
        logoutModal.close();
});
