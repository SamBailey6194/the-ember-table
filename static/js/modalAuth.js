document.addEventListener("DOMContentLoaded", () => {
  // Get modal elements
  const loginModal = document.getElementById("login-modal");
  const signupModal = document.getElementById("signup-modal");
  const closeLoginBtn = document.getElementById("close-login");
  const closeSignupBtn = document.getElementById("close-signup");
  const switchToSignupBtn = document.getElementById("switch-to-signup");
  const switchToLoginBtn = document.getElementById("switch-to-login");

  // Open login modal
  document.querySelectorAll(".login-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      loginModal.showModal();
    });
  });

  // Open signup modal
  document.querySelectorAll(".signup-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      signupModal.showModal();
    });
  });

  if (closeLoginBtn) closeLoginBtn.addEventListener("click", () => loginModal.close());
  if (closeSignupBtn) closeSignupBtn.addEventListener("click", () => signupModal.close());

  // Switch from login to signup
  if (switchToSignupBtn) {
    switchToSignupBtn.addEventListener("click", () => {
      loginModal.close();
      signupModal.showModal();
    });
  }

  // Switch from signup to login
  if (switchToLoginBtn) {
    switchToLoginBtn.addEventListener("click", () => {
      signupModal.close();
      loginModal.showModal();
    });
  }
});

