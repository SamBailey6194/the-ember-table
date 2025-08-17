/**
 * @jest-environment jsdom
 */

import fs from 'fs';
import path from 'path';
import '../static/js/modalAuth.js'; // your JS file

describe('Modal Auth JS', () => {
    let html;

    beforeEach(() => {
        html = fs.readFileSync(path.resolve(__dirname, 'user/templates/included/modal_auth_fixture.html'), 'utf8');
        document.documentElement.innerHTML = html;
        require('static/js/modalAuth.js');
    });

    test('Login trigger opens login modal', () => {
        const loginBtn = document.querySelector('.login-btn');
        const loginModal = document.getElementById('login-modal');

        expect(loginModal.open).toBeFalsy();
        loginBtn.click();
        expect(loginModal.open).toBeTruthy();
    });

    test('Signup trigger opens signup modal', () => {
        const signupBtn = document.querySelector('.signup-btn');
        const signupModal = document.getElementById('signup-modal');

        expect(signupModal.open).toBeFalsy();
        signupBtn.click();
        expect(signupModal.open).toBeTruthy();
    });

    test('Switch from login to signup', () => {
        const loginModal = document.getElementById('login-modal');
        const signupModal = document.getElementById('signup-modal');
        const switchBtn = document.getElementById('switch-to-signup');

        loginModal.showModal();
        expect(loginModal.open).toBeTruthy();
        expect(signupModal.open).toBeFalsy();

        switchBtn.click();

        expect(loginModal.open).toBeFalsy();
        expect(signupModal.open).toBeTruthy();
    });

    test('Switch from signup to login', () => {
        const loginModal = document.getElementById('login-modal');
        const signupModal = document.getElementById('signup-modal');
        const switchBtn = document.getElementById('switch-to-login');

        signupModal.showModal();
        expect(signupModal.open).toBeTruthy();
        expect(loginModal.open).toBeFalsy();

        switchBtn.click();

        expect(signupModal.open).toBeFalsy();
        expect(loginModal.open).toBeTruthy();
    });

    test('Close buttons close modals', () => {
        const loginModal = document.getElementById('login-modal');
        const signupModal = document.getElementById('signup-modal');
        const closeLogin = document.getElementById('close-login');
        const closeSignup = document.getElementById('close-signup');

        loginModal.showModal();
        signupModal.showModal();

        closeLogin.click();
        closeSignup.click();

        expect(loginModal.open).toBeFalsy();
        expect(signupModal.open).toBeFalsy();
    });
});