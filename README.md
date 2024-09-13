# LOTR Characters API

Esta é uma API baseada em FastAPI para gerenciar personagens, raças, classes e cidades do universo "O Senhor dos Anéis" (LOTR). A API utiliza SQLAlchemy para interagir com um banco de dados SQLite, com funcionalidades CRUD (Create, Read, Update, Delete) para cada entidade.

## Funcionalidades

- CRUD para Personagens
- CRUD para Raças
- CRUD para Classes
- CRUD para Cidades

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework de API web rápida e moderna.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Biblioteca SQL para Python usada para ORM (Object Relational Mapping).
- **[SQLite](https://www.sqlite.org/index.html)**: Banco de dados SQL leve.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Para validação de dados e tipagem usando Python.
- **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI para rodar o FastAPI.

## Requisitos

- Python 3.12+
- PIP (gerenciador de pacotes do Python)
- Poetry (opcional, se você estiver usando o Poetry para gerenciar dependências)

## Instalação

### Clonar o repositório

```bash
git clone https://github.com/Vicrrs/LOTR_characters.git
cd LOTR_characters
