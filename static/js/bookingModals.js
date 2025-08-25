document.addEventListener('DOMContentLoaded', () => {
    /**
     * Handles the "Make Booking" modal:
     * - Opens when a trigger button is clicked.
     * - Closes when any close button inside the modal is clicked.
     */
    const makeBookingModal = document.getElementById('make-booking-modal');
    document.querySelectorAll('[onclick*="make-booking-modal"]').forEach(btn => {
        btn.addEventListener('click', () => {
            makeBookingModal.showModal();
        });
    });

    const closeBtns = makeBookingModal?.querySelectorAll('button[type="button"]');
    closeBtns?.forEach(btn => {
        btn.addEventListener('click', () => makeBookingModal.close());
    });

    /**
     * Success Modal:
     * - Displays automatically on page load if a reference code exists.
     */
    const successModal = document.getElementById('success-modal');
    if (successModal) {
        const refCode = successModal.querySelector('span');
        if (refCode && refCode.textContent.trim() !== '') {
            successModal.showModal();
        }
    }

    /**
     * Cancel Booking Modal:
     * - Opens when a button with a `data-ref` attribute is clicked.
     * - Populates a hidden input with the booking reference code.
     */
    const cancelModal = document.getElementById("booking-cancelled-modal");
    const cancelCloseBtn = document.getElementById('close-cancel-btn');
    document.querySelectorAll("[data-ref]").forEach(btn => {
        btn.addEventListener("click", () => {
            if (!cancelModal) return;
            const hiddenInput = cancelModal.querySelector("input[name='reference_code']");
            if (hiddenInput) hiddenInput.value = btn.dataset.ref;
            cancelModal.showModal();
        });
    });

    // Close modal
    if (cancelCloseBtn && cancelModal) {
        cancelCloseBtn.addEventListener('click', () => {
            cancelModal.close();
        });
    }

    /**
     * Update Booking Modal:
     * - Opens when an `.update-btn` is clicked.
     * - Populates the update form with booking details from dataset attributes.
     * - Closes the modal when the form is submitted or when cancel is clicked.
     */
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

            updateModal.showModal();
        });
    });

    if (updateForm) {
        updateForm.addEventListener('submit', () => {
            updateModal.close();
        });
    }

    const updateCancelBtn = document.getElementById('update-cancel-btn');
    if (updateCancelBtn) {
        updateCancelBtn.addEventListener('click', () => updateModal.close());
    }
});