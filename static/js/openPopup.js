function openPopup(button) {
    var itemId = button.getAttribute("data-item-id");
    var listaId = button.getAttribute("data-lista-id");
    var earningId = button.getAttribute('data-earning-id');
    var itemName = "";
    var listaName = "";

    if (itemId) {
        itemName = button.closest('.item-container').querySelector('.details p').innerText;
        var itemWords = itemName.split(" ");
        var filteredName = itemWords.slice(1).join(" ");
        var form = document.getElementById("delete-form");
        var actionUrl = `deletar/${itemId}/`;
        form.setAttribute("action", actionUrl);
        document.getElementById("item-name").innerText = filteredName;
    } else if (listaId) {
        listaName = button.closest('.list-container').querySelector('.details a').innerText;
        var form = document.getElementById("delete-form");
        var actionUrl = `${listaId}/deletar/`;
        form.setAttribute("action", actionUrl);
        document.getElementById("lista-name").innerText = listaName;
    } else if (earningId) {
        var form = document.getElementById("delete-form");
        var actionUrl = `deletar/${earningId}/`;
        form.setAttribute('action', actionUrl);
        document.getElementById('item-name');
    }

    document.getElementById("popup").style.display = "block";

    document.addEventListener("keydown", handleKeyDown);
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
    document.removeEventListener("keydown", handleKeyDown);
}

function handleKeyDown(event) {
    if (event.key === "Escape") {
        closePopup();
    }
}
