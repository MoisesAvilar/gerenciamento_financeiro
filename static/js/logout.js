document.addEventListener("DOMContentLoaded", function() {
    var logoutLink = document.getElementById("logout");

    logoutLink.addEventListener("click", function(event) {
        var confirmLogout = confirm("Você realmente deseja sair?");
        if (!confirmLogout) {
            event.preventDefault();
        }
    });
});