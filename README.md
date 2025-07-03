# Gerenciamento Financeiro Pessoal

Uma aplicação web moderna e completa, construída com Django, para um gerenciamento financeiro pessoal intuitivo e eficaz. A plataforma foi totalmente refatorada para oferecer uma experiência de usuário limpa, responsiva e com funcionalidades avançadas.

## 🚀 Aplicação Ao Vivo

Você pode testar a aplicação completa, incluindo o login com Google e o novo design, no link abaixo:

[![Acessar Aplicação](https://img.shields.io/badge/Acessar-Aplicação_Online-brightgreen?style=for-the-badge)](http://expenses.pythonanywhere.com/)

## Funcionalidades Principais

-   **Autenticação Social e Segura:**
    -   **Login com Google:** Cadastro e login rápidos e seguros com apenas um clique, utilizando a conta do Google.
    -   **Sistema de Contas Tradicional:** Sistema de cadastro e login com usuário e senha totalmente funcional.
    -   **Configuração Segura:** Uso de variáveis de ambiente para proteger dados sensíveis como a `SECRET_KEY`.

-   **Interface Moderna com Modo Escuro:**
    -   **Design Renovado:** Todas as telas, do painel de controle aos formulários, foram redesenhadas para uma interface mais profissional e agradável.
    -   **Modo Escuro:** Um seletor de tema (claro/escuro) está disponível em toda a aplicação para maior conforto visual.
    -   **Componentes Interativos:** A interface utiliza cards, modais e ícones para facilitar a navegação e o uso.

-   **Gerenciamento de Despesas:**
    -   **Listas de Gastos:** Crie e gerencie múltiplas listas para organizar suas despesas (ex: "Compras do Mês", "Gastos com Lazer").
    -   **Operações CRUD Completas:** Adicione, visualize, edite e delete listas e itens de forma intuitiva.

-   **Controle de Ganhos:**
    -   Registre e acompanhe suas fontes de renda, salários e ganhos extras.

-   **Exportação de Dados:**
    -   Exporte os dados das suas listas de gastos para arquivos Excel (.xlsx) para análises externas.

-   **Relatórios e Gráficos:**
    -   _(Em progresso)_ Seção futura para visualização de dados financeiros através de gráficos interativos.

## Tecnologias e Boas Práticas

-   **Back-end:** Django
-   **Front-end:** Bootstrap 5, HTML5, CSS3, JavaScript
-   **Autenticação:** `django-allauth` para autenticação social.
-   **Segurança:** `python-dotenv` para gerenciamento de variáveis de ambiente.
-   **Banco de Dados:** SQLite3 (desenvolvimento), facilmente portável para PostgreSQL ou MySQL.

## Instalação

Para executar esta aplicação em sua máquina local, siga estas etapas:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MoisesAvilar/gerenciamento-financeiro.git](https://github.com/MoisesAvilar/gerenciamento-financeiro.git)
    cd gerenciamento-financeiro
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Configure as Variáveis de Ambiente:**
    -   Este projeto usa um arquivo `.env` para configurações de segurança. Crie uma cópia do arquivo de exemplo:
        ```bash
        # Para Windows
        copy .env.example .env

        # Para macOS/Linux
        cp .env.example .env
        ```
    -   Abra o novo arquivo `.env` e, se desejar, altere a `SECRET_KEY` (opcional para desenvolvimento).

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário (opcional):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

---