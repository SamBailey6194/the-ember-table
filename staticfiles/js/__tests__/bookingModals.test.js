const fs = require('fs');
const path = require('path');
require('../bookingModals.js');

const html = fs.readFileSync(path.resolve(__dirname, '../__html_fixtures__/booking_modals.html'), 'utf8');

beforeEach(() => {
    document.body.innerHTML = html;

    const updateBtn = document.createElement('button');
    updateBtn.className = 'update-btn';
    updateBtn.dataset.bookingId = '1';
    updateBtn.dataset.reference = 'ABC123';
    updateBtn.dataset.date = '2025-08-28';
    updateBtn.dataset.time = '12:00';
    updateBtn.dataset.partySize = '4';
    document.body.appendChild(updateBtn);

    document.querySelectorAll('dialog').forEach(modal => {
        modal.showModal = jest.fn(() => { modal.open = true; });
        modal.close = jest.fn(() => { modal.open = false; });
    });

    document.dispatchEvent(new Event('DOMContentLoaded'));
});

describe('bookingModals.js', () => {

    test('Cancel Booking Modal opens and closes', () => {
        const cancelModal = document.getElementById('booking-cancelled-modal');
        const cancelBtn = document.querySelector('[data-ref="12345"]');
        const closeBtn = document.getElementById('close-cancel-btn');

        cancelBtn.click();
        expect(cancelModal.showModal).toHaveBeenCalled();
        expect(cancelModal.open).toBe(true);
        expect(cancelModal.querySelector("input[name='reference_code']").value).toBe('12345');

        closeBtn.click();
        expect(cancelModal.close).toHaveBeenCalled();
        expect(cancelModal.open).toBe(false);
    });

    test('Update Booking Modal opens and populates form', () => {
        const updateModal = document.getElementById('update-booking-modal');
        const updateForm = document.getElementById('update-booking-form');

        const updateBtn = document.querySelector('.update-btn');
        updateBtn.click();

        expect(updateModal.showModal).toHaveBeenCalled();
        expect(updateModal.open).toBe(true);

        expect(updateForm.querySelector("input[name='booking_id']").value).toBe('1');
        expect(updateForm.querySelector("input[name='reference_code']").value).toBe('ABC123');
        expect(updateForm.querySelector("input[name='date']").value).toBe('2025-08-28');
        expect(updateForm.querySelector("input[name='time']").value).toBe('12:00');
        expect(updateForm.querySelector("input[name='party_size']").value).toBe('4');

        const cancelBtn = document.getElementById('update-cancel-btn');
        cancelBtn.click();
        expect(updateModal.close).toHaveBeenCalled();
        expect(updateModal.open).toBe(false);
    });

    test('Update form submission closes modal', () => {
        const updateModal = document.getElementById('update-booking-modal');
        const updateForm = document.getElementById('update-booking-form');

        updateModal.showModal();
        updateForm.dispatchEvent(new Event('submit'));

        expect(updateModal.close).toHaveBeenCalled();
        expect(updateModal.open).toBe(false);
    });
});
