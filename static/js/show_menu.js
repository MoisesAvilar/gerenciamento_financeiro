function clickMenu() {
    var info = document.getElementById('info');

    if (info.style.display === 'block') {
        info.style.display = 'none';
    } else {
        info.style.display = 'block';
    }
}

document.addEventListener('click', function(event) {
    var info = document.getElementById('info');
    var menu = document.getElementById('menu');

    if (!info.contains(event.target) && event.target !== menu) {
        info.style.display = 'none';
    }
});