// openPopup.js (nova versão)

document.addEventListener('DOMContentLoaded', function () {
    const deleteModalElement = document.getElementById('deleteConfirmationModal');
    
    if (deleteModalElement) {
        // Escuta o evento que o Bootstrap dispara ANTES de o modal ser exibido
        deleteModalElement.addEventListener('show.bs.modal', function (event) {
            
            // Pega o botão que acionou o modal
            const button = event.relatedTarget;

            // Extrai a URL de exclusão e o nome do item dos atributos 'data-*' do botão
            const formAction = button.getAttribute('data-form-action');
            const itemName = button.getAttribute('data-item-name');

            // Encontra os elementos dentro do modal que vamos atualizar
            const deleteForm = deleteModalElement.querySelector('#delete-form');
            const itemNameElement = deleteModalElement.querySelector('#delete-item-name');

            // Atualiza a 'action' do formulário com a URL correta
            deleteForm.setAttribute('action', formAction);

            // Atualiza o texto de confirmação com o nome do item
            if (itemName) {
                itemNameElement.textContent = `"${itemName}"`;
            } else {
                itemNameElement.textContent = 'este registro';
            }
        });
    }
});