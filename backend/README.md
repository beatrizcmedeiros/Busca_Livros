# Busca Livros - Servidor

Essa parte fica responsável por acessar a API do Google Books e do Twitter e trazer os dados necessários de cada uma. Na API do Google Books será utilizado o nome do livro, que será passado na hora que a requisição for feita, o nome do autor ou autora e a descrição referente ao livro. Já na API do twitter, será buscado os twitees que fizerem referencia ao nome do livro pesquisado, pegando também o usuário que realizou o comentario.

### 📋 Pré-requisitos

Como serão necessários dois aquivos python para a execução do projeto, primeiramente iremos tratar o arquivo 'apis.py'. Nele será necessário importar as seguintes bibliotecas: 'tweepy' e 'requests'. A primeira para lidar com a API do Twitter e a segunda para lidar com as requisições que serão feitas para as APIs.
Em seguida para conseguir executar o arquivo 'apisFk.py' as seguintes bibiotecas devem ser importadas: 'flask', 'flask_cors', 'json'. As duas primeiras são necessárias para criar uma rota de conexão onde será feita a requisição, a ultima para que seja possível receber e enviar o JSON gerado pela API.

### 🔧 Instalação

Para importar as bibliotecas é necessário ter o 'pip' instalado no seu computador, caso tenha basta dar o seguinte comando no terminal, formado por 'pip install' mais o nome da biblioteca que deseja instalar. 

Exemplos:
'pip install tweepy'
'pip install requests'
'pip install flask'
'pip install flask_cors'
'pip install json'

## ⚙️ Executando os testes

Para verificar se as bibliotecas foram instaladas corretamente você pode acessar o terminal python, digitar 'import tweepy' e dar enter, caso não apareça nenhuma mensagem de erro, a instalação da biblioteca foi realizada com sucesso.

## 🛠️ Construído com

* API do Google Books
* API do Twitter
* API gerada a partir das citadas a cima


