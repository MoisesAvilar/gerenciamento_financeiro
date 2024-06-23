function logout() {
    let confirmLogout = confirm('Realmente deseja sair?')
    if (!confirmLogout) {
        event.preventDefault()
    }
}
