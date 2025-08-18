document.addEventListener('DOMContentLoaded', () => {
    // Make Booking Modal
    const makeBookingModal = document.getElementById('make-booking-modal');
    const makeBookingBtn = document.getElementById('make-booking-btn');

    if (makeBookingBtn && makeBookingModal) {
        makeBookingBtn.addEventListener('click', () => makeBookingModal.showModal());
    }

    // Booking form AJAX submit
    const bookingForm = makeBookingModal?.querySelector('form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(bookingForm);

            try {
                const response = await fetch(bookingForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    makeBookingModal.close();
                    bookingForm.reset();

                    const successModal = document.getElementById('success-modal');
                    if (successModal) {
                        const refCodeSpan = successModal.querySelector('span');
                        if (refCodeSpan) {
                            refCodeSpan.textContent = data.reference_code;
                        }
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

    // Show success modal on page load if reference code exists (fallback)
    const successModal = document.getElementById('success-modal');
    if (successModal) {
        const refCode = successModal.querySelector('span');
        if (refCode && refCode.textContent.trim() !== '') {
            successModal.showModal();
        }
    }
});