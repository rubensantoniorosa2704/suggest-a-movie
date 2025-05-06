# Flask Movie Recommendation App

Este é um projeto Flask que recomenda filmes semelhantes com base em um filme escolhido pelo usuário. A recomendação é feita com base em várias características dos filmes, como gênero, palavras-chave, popularidade, idioma e média de votos.

## Funcionalidade

O sistema calcula a similaridade entre filmes e retorna as 5 melhores recomendações para um filme selecionado pelo usuário.

## Dependências

Antes de rodar o projeto, instale as dependências listadas no arquivo `requirements.txt`:

Se você estiver usando Docker, as dependências serão automaticamente instaladas no processo de construção da imagem.

## Rodando a Aplicação

### Com Docker

1. **Construir a Imagem Docker**

   Use o comando abaixo para construir a imagem Docker:

   ```bash
   make build
   ```

2. **Rodar o Container Docker**

    Depois de construir a imagem, rode o container:

    ```bash
    make run
    ```

    A aplicação estará disponível em http://localhost:5000.

### Sem Docker

**Importante:** é necessário ter o Python 3 instalado em sua máquina antes de executar os próximos passos.

Se você preferir rodar o Flask diretamente, instale as dependências e execute o servidor manualmente:

1. **Configurar ambiente virtual**

    Use o comando abaixo para criar um ambiente virtual do python:

    ```bash
    > python -m venv venv
    ```

* Windows 
    
    Ative o ambiente virtual com o seguinte comando:

    ```bash
    > .venv/Scripts/activate
    ```

* Linux 
    
    Ative o ambiente virtual com o seguinte comando:

    ```bash
    > source venv/bin/activate
    ```

2. **Instalar dependências**

    Na raiz do projeto, use o seguinte comando:

    ```bash
    > pip install -r requirements.txt
    ```

3. **Iniciar o servidor Flask**

    Após instalar as dependências necessárias, simplesmente rode:

    ```bash
    > python main.py
    ```

    A aplicação estará disponível em http://localhost:5000.

## Utilização do endpoint:

A recomendação de filmes é feita através de uma requisição POST para o endpoint /recommend. O corpo da requisição contém o movie_id do filme para o qual as recomendações devem ser feitas.

### Formato da requisição:

```json
{
  "movie_id": <ID_DO_FILME>
}
```

A resposta será um JSON contendo o título dos filmes recomendados e a similaridade com o filme escolhido:

```json
[
    {
        "similarity": 0.965295505285367,
        "title": "Toy Story 2"
    },
    {
        "similarity": 0.9414378224485067,
        "title": "Toy Story 3"
    },
    {
        "similarity": 0.9321832474689741,
        "title": "Ratatouille"
    },
    {
        "similarity": 0.926615473479304,
        "title": "Finding Nemo"
    },
    {
        "similarity": 0.9257786043042225,
        "title": "Hotel Transylvania 2"
    }
]
```

Onde a similarity é um valor entre 0 e 1, indicando o quão semelhante o filme recomendado é ao filme escolhido.

## Comandos Úteis

O projeto inclui um Makefile para facilitar o uso de Docker. Aqui estão os comandos:

* build: Construir a imagem Docker:

    ```bash
    make build
    ```

* run: Rodar o container Docker:

    ```bash
    make run
    ```

* stop: Parar o container Docker em execução:

    ```bash
    make stop
    ```

* clean: Parar e deletar o container:

    ```bash
    make clean

* delete-image: Deletar a imagem Docker:

    ```bash
    make delete-image
    ```

## Contribuições

Contribuições são bem-vindas! Se você tiver ideias ou melhorias, fique à vontade para criar uma issue ou enviar um pull request.