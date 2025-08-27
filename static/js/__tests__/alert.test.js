/**
 * @jest-environment jsdom
 */

const fs = require('fs');
const path = require('path');
require('../alert.js');

const html = fs.readFileSync(path.resolve(__dirname, '../__html_fixtures__/alert.html'), 'utf8');

beforeEach(() => {
    document.body.innerHTML = html;

    const modal = document.getElementById('message-modal');
    modal.showModal = jest.fn(() => {
        modal.open = true;
    });
    modal.close = jest.fn(() => {
        modal.open = false;
    });

    document.dispatchEvent(new Event('DOMContentLoaded'));
});

describe('alert.js', () => {
    test('showMessage sets title and body and opens modal', () => {
        window.showMessage('Test Title', 'Test Body');

        const modal = document.getElementById('message-modal');
        const title = document.getElementById('message-title');
        const body = document.getElementById('message-body');

        expect(title.textContent).toBe('Test Title');
        expect(body.innerHTML).toBe('Test Body');
        expect(modal.open).toBe(true);
    });
});