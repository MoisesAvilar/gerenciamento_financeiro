function showLogoutButton() {
  const logout = document.getElementById("logout");

  if (logout.style.display === "none") {
    logout.style.display = "flex";
    document.addEventListener("click", handleClickOutside, true);
  } else {
    logout.style.display = "none";
    document.removeEventListener("click", handleClickOutside, true);
  }
}

function handleClickOutside(event) {
  const logout = document.getElementById("logout");
  const hello = document.getElementById("hello");
  if (!logout.contains(event.target) && !hello.contains(event.target)) {
    logout.style.display = "none";
    document.removeEventListener("click", handleClickOutside, true);
  }
}
