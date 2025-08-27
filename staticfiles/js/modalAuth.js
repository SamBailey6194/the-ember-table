document.addEventListener("DOMContentLoaded", () => {
  /**
   * Authentication modals: login & signup
   * - Each modal can be opened, closed, or switched between.
   * - The `next` field is dynamically set so users return to the correct page after login/signup.
   */
  const loginModal = document.getElementById("login-modal");
  const signupModal = document.getElementById("signup-modal");
  const closeLoginBtn = document.getElementById("close-login");
  const closeSignupBtn = document.getElementById("close-signup");
  const switchToSignupBtn = document.getElementById("switch-to-signup");
  const switchToLoginBtn = document.getElementById("switch-to-login");

  // Open login modal
  document.querySelectorAll(".login-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const nextUrl = btn.dataset.next || "/";
      const loginNextInput = loginModal.querySelector("input[name='next']");
      if (loginNextInput) loginNextInput.value = nextUrl;
      loginModal.showModal();
    });
  });

  // Open signup modal
  document.querySelectorAll(".signup-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const nextUrl = btn.dataset.next || "/";
      const signUpNextInput = signupModal.querySelector("input[name='next']");
      if (signUpNextInput) signUpNextInput.value = nextUrl;
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