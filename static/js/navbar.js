const burgerBtn = document.getElementById('burger-btn');
const mobileMenu = document.getElementById('mobile-menu');
const logoutModal = document.getElementById('logout-modal');
const openLogoutBtns = document.querySelectorAll('[data-open-logout]');
const closeLogoutBtn = document.getElementById('close-logout');

burgerBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

openLogoutBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        if (logoutModal.showModal) {
            logoutModal.showModal();
        } else {
            alert("The dialog API is not supported in this browser.");
        }
    });
});

closeLogoutBtn.addEventListener('click', () => {
        logoutModal.close();
});
