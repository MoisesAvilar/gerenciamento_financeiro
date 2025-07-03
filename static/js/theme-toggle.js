// theme-toggle.js (versão corrigida para Bootstrap Icons)

document.addEventListener("DOMContentLoaded", function() {
    const themeToggleButton = document.getElementById('toggle-theme');
    const themeIcon = document.getElementById('theme-icon'); 
    
    // Pega o tema salvo no localStorage ou define 'light' como padrão
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Função que aplica o tema no site
    const applyTheme = (theme) => {
        // Define o atributo data-bs-theme no elemento <html>
        document.documentElement.setAttribute('data-bs-theme', theme);
        // Salva a preferência no localStorage
        localStorage.setItem('theme', theme);

        // Troca as classes do Bootstrap Icons
        if (theme === 'dark') {
            themeIcon.classList.remove('bi-moon-fill');
            themeIcon.classList.add('bi-sun-fill');
        } else {
            themeIcon.classList.remove('bi-sun-fill');
            themeIcon.classList.add('bi-moon-fill');
        }
    };

    // Aplica o tema inicial quando a página carrega
    applyTheme(currentTheme);

    // Adiciona o evento de clique no botão
    if(themeToggleButton) {
        themeToggleButton.addEventListener('click', () => {
            // Verifica qual é o tema atual e define o novo tema
            const newTheme = document.documentElement.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
            applyTheme(newTheme);
        });
    }
});