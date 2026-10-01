# 📦 Achados e Perdidos

Aplicação web desenvolvida em **Python, Flask e SQLite** para criar um mural de achados e perdidos.

O sistema permite cadastrar objetos perdidos ou encontrados, visualizar os itens cadastrados, pesquisar por palavras-chave, filtrar os resultados e marcar itens como resolvidos.

## 🚀 Funcionalidades

* ✅ Cadastrar item perdido
* ✅ Cadastrar item encontrado
* ✅ Informar nome do item
* ✅ Informar descrição
* ✅ Informar local
* ✅ Informar contato
* ✅ Visualizar itens cadastrados
* ✅ Filtrar por:

  * Todos
  * Perdidos
  * Encontrados
* ✅ Pesquisar por palavra-chave
* ✅ Marcar item como resolvido
* ✅ Exibir mensagens de feedback
* ✅ Armazenar os dados em banco SQLite

## 🛠️ Tecnologias utilizadas

* **Python**
* **Flask**
* **SQLite**
* **HTML5**
* **CSS3**
* **Jinja2**

## 📁 Estrutura do projeto

```text
achados-perdidos/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── cadastrar.html
│
└── static/
    └── style.css
```

O arquivo `achados.db` é criado automaticamente quando a aplicação é executada.

## 💻 Como instalar e executar

### 1. Clonar o projeto

```bash
git clone https://github.com/jlvarejao/mini-app-achados.git
```

Entre na pasta:

```bash
cd mini-app-achados
```

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python app.py
```

### 5. Acessar no navegador

Abra:

```text
http://127.0.0.1:5000
```

## 📋 Como utilizar

### Cadastrar um item

Clique em **"Cadastrar item"** e informe:

* Tipo: perdido ou encontrado
* Nome do item
* Descrição
* Local
* Contato

Depois clique em **"Cadastrar"**.

### Pesquisar

Digite uma palavra no campo de busca.

A pesquisa pode encontrar informações relacionadas ao:

* Nome
* Descrição
* Local

### Filtrar

É possível visualizar:

* Todos os itens
* Apenas itens perdidos
* Apenas itens encontrados

### Resolver um item

Quando o objeto for devolvido ou a situação for resolvida, clique em:

**"Marcar como resolvido"**

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenar os dados.

A tabela principal é:

```text
itens
```

Ela possui os seguintes campos:

| Campo     | Descrição                         |
| --------- | --------------------------------- |
| id        | Identificador do item             |
| tipo      | Perdido ou encontrado             |
| nome      | Nome do objeto                    |
| descricao | Descrição do objeto               |
| local     | Local onde foi perdido/encontrado |
| contato   | Forma de contato                  |
| status    | Pendente ou Resolvido             |

## 🎯 Objetivo do projeto

O objetivo é desenvolver uma aplicação simples para facilitar a divulgação e a recuperação de objetos perdidos ou encontrados, utilizando tecnologias de desenvolvimento web com Python.

## 👨‍💻 Autor

Projeto desenvolvido para atividade acadêmica do SENAI.

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
