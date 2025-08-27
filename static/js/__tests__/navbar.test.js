/**
 * @jest-environment jsdom
 */

const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(
  path.resolve(__dirname, '../__html_fixtures__/navbar.html'),
  'utf8'
);

beforeEach(() => {
    document.body.innerHTML = html;

    const logoutModal = document.getElementById('logout-modal');
    if (logoutModal) {
        logoutModal.showModal = jest.fn(() => { logoutModal.open = true; });
        logoutModal.close = jest.fn(() => { logoutModal.open = false; });
    }

    jest.resetModules();
    require('../navbar.js');
});

describe('navbar.js', () => {
    test('Burger menu toggles mobile menu visibility', () => {
        const burgerBtn = document.getElementById('burger-btn');
        const mobileMenu = document.getElementById('mobile-menu');

        expect(mobileMenu.classList.contains('hidden')).toBe(true);

        burgerBtn.click();
        expect(mobileMenu.classList.contains('hidden')).toBe(false);

        burgerBtn.click();
        expect(mobileMenu.classList.contains('hidden')).toBe(true);
    });

    test('Logout modal opens when logout button clicked', () => {
        const logoutBtn = document.querySelector('[data-open-logout]');
        const logoutModal = document.getElementById('logout-modal');

        logoutBtn.click();
        expect(logoutModal.showModal).toHaveBeenCalled();
        expect(logoutModal.open).toBe(true);
    });

    test('Logout modal closes when close button clicked', () => {
        const closeBtn = document.getElementById('close-logout');
        const logoutModal = document.getElementById('logout-modal');

        logoutModal.showModal();
        expect(logoutModal.open).toBe(true);

        closeBtn.click();
        expect(logoutModal.close).toHaveBeenCalled();
        expect(logoutModal.open).toBe(false);
    });
});