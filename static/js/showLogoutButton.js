function showLogoutButton() {
  const logout = document.getElementById("logout");

  if (window.getComputedStyle(logout).display === "none") {
    logout.style.display = "flex";
    document.addEventListener("click", handleClickOutside);
  } else {
    logout.style.display = "none";
    document.removeEventListener("click", handleClickOutside);
  }
}

function handleClickOutside(event) {
  const logout = document.getElementById("logout");
  const hello = document.getElementById("hello");

  if (!logout.contains(event.target) && !hello.contains(event.target)) {
    logout.style.display = "none";
    document.removeEventListener("click", handleClickOutside);
  }
}
