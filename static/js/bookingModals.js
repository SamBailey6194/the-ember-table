document.addEventListener('DOMContentLoaded', () => {
    // Make Booking Modal
    const makeBookingModal = document.getElementById('make-booking-modal');
    document.querySelectorAll('[onclick*="make-booking-modal"]').forEach(btn => {
        btn.addEventListener('click', () => {
            makeBookingModal.showModal();
        });
    });

    // Close Make Booking Modal
    const closeBtns = makeBookingModal?.querySelectorAll('button[type="button"]');
    closeBtns?.forEach(btn => {
        btn.addEventListener('click', () => makeBookingModal.close());
    });

    // Success Modal on Page Load
    const successModal = document.getElementById('success-modal');
    if (successModal) {
        const refCode = successModal.querySelector('span');
        if (refCode && refCode.textContent.trim() !== '') {
            successModal.showModal();
        }
    }

    // Cancel Booking Modal shown on click
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

            updateModal.showModal();
        });
    });

    const updateCancelBtn = document.getElementById('update-cancel-btn');
    if (updateCancelBtn) {
        updateCancelBtn.addEventListener('click', () => updateModal.close());
    }
});