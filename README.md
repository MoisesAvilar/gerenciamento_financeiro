# Gerenciamento Financeiro

Esta é uma aplicação Django projetada para auxiliar no controle de gastos mensais e no gerenciamento financeiro pessoal. Ela oferece as seguintes funcionalidades principais:

- **Listas e Itens:** A aplicação permite a criação de listas para categorizar suas despesas e a adição de itens associados a cada lista. Isso facilita a organização e o rastreamento de gastos.

- **Operações CRUD:** As operações CRUD (Criar, Ler, Atualizar e Deletar) estão disponíveis tanto para listas quanto para itens. Isso oferece flexibilidade para adicionar, visualizar, atualizar e excluir informações de maneira intuitiva.

## Recursos Adicionais

Aqui estão alguns dos recursos adicionais e funcionalidades que você pode encontrar nesta aplicação:

- **Rastreamento de Gastos em Tempo Real:** A aplicação oferece uma visão em tempo real do quanto você já gastou em relação ao seu orçamento atual, fornecendo uma análise clara da situação financeira.

- **Categorização de Despesas:** Categorize suas despesas em diferentes categorias, tornando mais fácil identificar onde seu dinheiro está sendo gasto.

- **Metas Financeiras:** Defina metas financeiras pessoais para economia ou redução de gastos, ajudando na motivação para alcançar objetivos financeiros.

- **Exportação de Dados:** Exporte seus dados financeiros para formatos compatíveis, como CSV, para análises mais avançadas no Excel ou em outras ferramentas.

- **Relatórios e Gráficos:** Visualize seus dados financeiros por meio de gráficos e relatórios interativos para uma compreensão mais profunda dos seus hábitos de gastos.

## Instalação

Para instalar e executar esta aplicação em sua máquina local, siga as seguintes etapas:

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/MoisesAvilar/gerenciamento-financeiro.git

2. Crie um ambiente virtual (recomendado) e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate

3. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt

4. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate

5. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver

6. Acesse a aplicação em seu navegador:
    
    ```bash
    http://localhost:8000/

7. Desfrute da aplicação!
