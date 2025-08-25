document.addEventListener("DOMContentLoaded", () => {
    const messageModal = document.getElementById("message-modal");
    const messageTitle = document.getElementById("message-title");
    const messageBody = document.getElementById("message-body");
    const closeButton = document.getElementById("close-message");

    // Close modal
    closeButton.addEventListener("click", () => messageModal.close());

    // Function to show modal dynamically
    window.showMessage = (title, body) => {
        messageTitle.textContent = title;
        messageBody.innerHTML = body;
        messageModal.showModal();
    };

    // Automatically show messages from Django
    try {
        const messages = JSON.parse(document.getElementById("django-messages").textContent);
        messages.forEach(msg => {
            const title = msg.tags.charAt(0).toUpperCase() + msg.tags.slice(1);
            showMessage(title, msg.message);
        });
    } catch (e) {
        console.error("No Django messages found or JSON parsing error:", e);
    }
});