import tweepy
import requests

#Chave de API do Google Books
api_key = "AIzaSyCrrzTaU-xgEF-NZg5d-bv8Rf-eVzRSTZ8"

#Autenticação do Twitter
consumer_key = "mPC7cD6bfXhuO1RrnpgPIhNdT"
consumer_secret = "xZSVsJIgGRJLycL9j2IFQwRCSm7bRVc0WQsNJXW74XOky2J453"
access_token = "4027730247-ErsDHt7SuvINOWMWgfoorG7hEfXzgeYNzrwvzZ7"
access_token_secret = "l7yn9GtaVpyZmMAxICEyEL2MMw23UYNuVO4VHikbAnJrN"

# Crie a autenticação do Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
# Crie o objeto API
api = tweepy.API(auth)

def apiGoogle(title):
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title['titulo']}&key={api_key}")

    informacoes = []

    if response.status_code == 200:
        data = response.json()

        for i in data['items']:
            if(title['titulo'].lower() in i['volumeInfo']['title'].lower()):
                titulo = i['volumeInfo']['title']
                titulo = titulo + " livro"
                for j in i['volumeInfo']['authors']:
                    autor = j
                descricao = i['volumeInfo']['description']
                break            
            else:
                titulo = i['volumeInfo']['title']
                response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{titulo}&key={api_key}")

                print(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{titulo}&key={api_key}")

                informacoes = []

                if response.status_code == 200:
                    data = response.json()

                    for i in data['items']:
                        if(titulo.lower() in i['volumeInfo']['title'].lower()):
                            titulo = i['volumeInfo']['title']
                            titulo = titulo + " livro"
                            for j in i['volumeInfo']['authors']:
                                autor = j
                            descricao = i['volumeInfo']['description']
                            break   
                        else:         
                            informacoes.append({'Erro': 'Não encontramos o livro "'+title['titulo']+'" no Google Books.'})
                            return informacoes
    else:
        print(f"Erro ao pesquisar por livros: {response.status_code}")

    tweets = []
    tweets = apiTwitter(titulo)

    informacoes.append({'Titulo': title, 'autor/autora': autor, 'descricao': descricao, 'tweets':tweets})

    return informacoes

def apiTwitter(titulo):
    results = api.search_tweets(
        q=titulo,
        lang="pt",
        tweet_mode="extended",
        count=100
    )

    tweetsArray = []

    if(len(results) == 0):
        tweetsArray.append({'Erro: ': 'Não encontramos nenhum comentário sobre o livro "' +titulo+ '" no Twitter.'})
    else:
        for tweet in results:
            user = tweet.user.screen_name
            comentario = tweet.full_text
            tweetsArray.append({'user': user, 'comentario': comentario})

    return tweetsArray

