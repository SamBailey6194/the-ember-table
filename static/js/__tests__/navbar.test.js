/**
 * @jest-environment jsdom
 */

const fs = require('fs');
const path = require('path');

beforeEach(() => {
    const html = fs.readFileSync(path.resolve(__dirname, 'fakeHtml.html'), 'utf8');
    document.documentElement.innerHTML = html;

    // Simulate dialog API
    HTMLDialogElement.prototype.showModal = jest.fn();
    HTMLDialogElement.prototype.close = jest.fn();

    // Require the script after setting up the DOM
    require('./script.js');
});

afterEach(() => {
    jest.resetModules();
});

test('Burger button toggles hidden class on mobile menu', () => {
    const burgerBtn = document.getElementById('burger-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    expect(mobileMenu.classList.contains('hidden')).toBe(true);

    burgerBtn.click();
    expect(mobileMenu.classList.contains('hidden')).toBe(false);

    burgerBtn.click();
    expect(mobileMenu.classList.contains('hidden')).toBe(true);
});

test('Clicking logout open buttons calls showModal', () => {
    const logoutModal = document.getElementById('logout-modal');
    const openBtns = document.querySelectorAll('[data-open-logout]');

    openBtns[0].click();
    expect(logoutModal.showModal).toHaveBeenCalled();

    openBtns[1].click();
    expect(logoutModal.showModal).toHaveBeenCalledTimes(2);
});

test('Clicking close logout button calls close', () => {
    const logoutModal = document.getElementById('logout-modal');
    const closeBtn = document.getElementById('close-logout');

    closeBtn.click();
    expect(logoutModal.close).toHaveBeenCalled();
});