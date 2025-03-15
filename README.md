# Star Wars API com Flask

Este projeto utiliza Flask para criar uma aplicação web que consome a API de personagens de Star Wars (SWAPI), complementando as informações com imagens dos personagens retiradas da página do Fandom Star Wars Wiki. A aplicação exibe informações sobre os personagens em uma interface web simples.

## Funcionalidades

- **Exibição de personagens de Star Wars**: A aplicação exibe uma lista de personagens com informações como nome, altura, peso, cor dos olhos, cor do cabelo, e ano de nascimento.
- **Imagens dos personagens**: A aplicação baixa imagens dos personagens a partir do Fandom Star Wars Wiki e as exibe no frontend.
- **API de busca por personagem**: A API permite buscar informações detalhadas de um personagem via endpoint `/api/character/<int:character_id>`.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **BeautifulSoup**: Biblioteca para realizar scraping de conteúdo HTML.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **Werkzeug**: Utilizado para segurança na manipulação de nomes de arquivos.
  
## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3.6 ou superior instalado na sua máquina. Você também precisará instalar as dependências necessárias.

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/star-wars-flask-api.git
    cd star-wars-flask-api
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação

Para rodar a aplicação, basta executar o seguinte comando:

```bash
python app.py
```

Endpoints da API
GET /api/character/int:character_id: Retorna informações de um personagem de Star Wars pelo ID.
Exemplo: GET http://127.0.0.1:5000/api/character/1
Retorno:

```json
{
  "name": "Luke Skywalker",
  "height": "172",
  "mass": "77",
  "hair_color": "blond",
  "eye_color": "blue",
  "birth_year": "19BBY",
  "image": "https://starwars.fandom.com/wiki/File:Luke_Skywalker.jpg"
}
```

Interface Web
Quando você acessar http://127.0.0.1:5000/ no seu navegador, verá uma página que exibe os personagens com seus respectivos dados e imagens, como mostrado abaixo:

Nome do Personagem
Altura
Peso
Cor do cabelo
Cor dos olhos
Ano de nascimento


### Como Funciona o Código

1. **Funcionalidade Principal**:
   - Quando você acessa o endpoint principal `/`, o servidor Flask faz requisições para a SWAPI para obter os personagens.
   - Para cada personagem, ele faz scraping no site Fandom Star Wars Wiki para buscar a imagem do personagem.
   - Caso a imagem ainda não tenha sido baixada, ela é salva na pasta `static/images`.

2. **Armazenamento de Imagens**:
   - As imagens são armazenadas no diretório `static/images`, e o nome do arquivo da imagem é associado ao personagem.
   - Se uma imagem já foi baixada, ela não é baixada novamente.

3. **Exibição de Personagens**:
   - As informações dos personagens, incluindo as imagens, são passadas para o template `index.html` para exibição na página.

### Como Funcionarão as Imagens

- **Imagens Baixadas**: Quando um personagem for exibido, a imagem será carregada a partir do diretório `static/images`.
- **Imagem Não Disponível**: Caso um personagem não tenha imagem ou não seja possível obter a imagem, um valor vazio (`''`) será atribuído ao campo `image_filename`, e você pode personalizar o que será exibido no template quando isso acontecer.

---

