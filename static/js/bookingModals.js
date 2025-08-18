document.addEventListener('DOMContentLoaded', () => {
    const successModal = document.getElementById('success-modal');

    // Show success modal only if it has a reference code
    if (successModal && successModal.querySelector('span').textContent.trim() !== '') {
        successModal.showModal();
    }
});