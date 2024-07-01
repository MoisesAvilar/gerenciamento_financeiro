function passwordVisibility(inputId, eyeId, eyeSlashId) {
  const eye = document.getElementById(eyeId);
  const eyeSlash = document.getElementById(eyeSlashId);
  const passwordInput = document.querySelector(`#${inputId}`);

  if (passwordInput && passwordInput.type === "password") {
    eye.style.display = "none";
    eyeSlash.style.display = "inline-block";
    passwordInput.type = "text";
  } else if (passwordInput) {
    eye.style.display = "inline-block";
    eyeSlash.style.display = "none";
    passwordInput.type = "password";
  } else {
    console.error("Campo de senha não encontrado!");
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const iconPairs = [
    { eye: "eye", eyeSlash: "eye-slash", inputId: "id_password" },
    { eye: "eye1", eyeSlash: "eye-slash1", inputId: "id_password1" },
    { eye: "eye2", eyeSlash: "eye-slash2", inputId: "id_password2" },
  ];

  iconPairs.forEach((pair) => {
    const eye = document.getElementById(pair.eye);
    const eyeSlash = document.getElementById(pair.eyeSlash);

    if (eye && eyeSlash) {
      eye.addEventListener("click", function () {
        passwordVisibility(pair.inputId, pair.eye, pair.eyeSlash);
      });
      eyeSlash.addEventListener("click", function () {
        passwordVisibility(pair.inputId, pair.eye, pair.eyeSlash);
      });
    }
  });
});
