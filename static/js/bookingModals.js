document.addEventListener('DOMContentLoaded', () => {
    // Make Booking Modal
    const makeBookingModal = document.getElementById('make-booking-modal');

    const bookingForm = makeBookingModal?.querySelector('form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(bookingForm);

            try {
                const response = await fetch(bookingForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: { 'X-Requested-With': 'XMLHttpRequest' }
                });

                if (response.ok) {
                    const data = await response.json();
                    makeBookingModal.close();
                    bookingForm.reset();

                    // Show success modal
                    const successModal = document.getElementById('success-modal');
                    if (successModal) {
                        const refCodeSpan = successModal.querySelector('span');
                        if (refCodeSpan) refCodeSpan.textContent = data.reference_code;
                        successModal.showModal();
                    }
                } else {
                    const errorText = await response.text();
                    console.error('Booking failed:', errorText);
                }
            } catch (err) {
                console.error('Booking error:', err);
            }
        });
    }

    // Success Modal on Page Load
    const successModal = document.getElementById('success-modal');
    if (successModal) {
        const refCode = successModal.querySelector('span');
        if (refCode && refCode.textContent.trim() !== '') {
            successModal.showModal();
        }
    }

    // Cancel Booking Modal shown on click
    document.querySelectorAll("[data-ref]").forEach(btn => {
        btn.addEventListener("click", () => {
            const cancelModal = document.getElementById("booking-cancelled-modal");
            const hiddenInput = cancelModal.querySelector("input[name='reference_code']");
            hiddenInput.value = btn.dataset.ref;
            cancelModal.showModal();
        });
    });

    // Update Modal shown on click
    const updateModal = document.getElementById('update-booking-modal');
    const updateForm = document.getElementById('update-booking-form');

    document.querySelectorAll('.update-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            updateForm.action = `/booking/updated/${btn.dataset.bookingId}/`;
            updateForm.querySelector("input[name='booking_id']").value = btn.dataset.bookingId;
            updateForm.querySelector("input[name='reference_code']").value = btn.dataset.reference;
            updateForm.querySelector("input[name='date']").value = btn.dataset.date;
            updateForm.querySelector("input[name='time']").value = btn.dataset.time;
            updateForm.querySelector("input[name='party_size']").value = btn.dataset.partySize;

            // Open modal
            updateModal.showModal();
        });
    });

    // Close modal
    document.getElementById('update-cancel-btn').addEventListener('click', () => {
        updateModal.close();
    });

    // Submit Updated Changes
    updateForm.addEventListener('submit', async e => {
        e.preventDefault();
        const formData = new FormData(updateForm);

        try {
            const response = await fetch(updateForm.action, {
                method: 'POST',
                body: formData,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });

            const data = await response.json();
            if (response.ok && data.success) {
                updateModal.close();
                alert(`Booking ${data.reference_code} updated successfully`);
            } else {
                alert('Update failed. Check console.');
                console.error(data);
            }
        } catch (err) {
            console.error('AJAX error', err);
        }
    });
});