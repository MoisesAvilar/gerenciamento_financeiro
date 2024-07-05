function openPopup(button) {
    var itemId = button.getAttribute("data-item-id");
    var listaId = button.getAttribute("data-lista-id");
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
    }

    document.getElementById("popup").style.display = "block";
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
}
