var req = new XMLHttpRequest();

const button = document.querySelector("#btn-buscar");
const input = document.querySelector("#nome-livro");

input.addEventListener("keypress", function(event){
    if(event.keyCode === 13){
        button.click();
    }
})

button.onclick = () => {
    const loading = document.querySelector("#loading")
    loading.style.display = 'inline-block'
    limpaResultado();

    const nomeLivro = input.value;

    req.onloadend = function(){
        const loading = document.querySelector("#loading");
        loading.style.display = 'none';
        try {
            const resp = req.responseText;
            respObj = JSON.parse(resp);
            resultado(respObj);
        } catch (error) {
            const main = document.querySelector("main");
            const msgError = document.createElement("h1");
            msgError.setAttribute("id", "msg-erro");
            msgError.innerHTML = "Ocorreu um erro na busca. Verifique sua pesquisa e tente novamente!"
            main.appendChild(msgError);
        }
    }

    req.open(
        "POST", 
        'http://127.0.0.1:5000'
    );

    req.setRequestHeader("Accept", "application/json");
    req.setRequestHeader("Content-Type", "application/json");

    const data = `{
        "titulo": "${nomeLivro}"
    }`;

    req.send(data);
}

function resultado(json){
    const infoLivro = document.querySelector("#info-livro");
    const infoTweets = document.querySelector("#info-tweets");

    infoLivro.style.display = "block";
    
    const tituloLivro = document.querySelector("#titulo-livro");
    tituloLivro.innerHTML = '"'+json[0]['Titulo']['titulo']+'"';

    const autor = document.querySelector("#nome-autor");
    autor.innerHTML = json[0]['autor/autora'];

    const descricao = document.querySelector("#text-descricao");
    descricao.innerHTML = json[0]['descricao'];

    const listaTweets = document.querySelector("#lista-tweets");

    infoTweets.style.display = "block";
    json[0]['tweets'].forEach(tweet => {
        const novoTweet = document.createElement("li");
        
        const userName = document.createElement("span");
        userName.className = "user-name";
        userName.innerHTML = tweet['user'];

        const comentario = document.createElement("span");
        comentario.setAttribute("id", "comentario");
        comentario.innerHTML = tweet['comentario']; 

        novoTweet.appendChild(userName);
        novoTweet.appendChild(comentario);

        if(tweet['comentario'])
            listaTweets.appendChild(novoTweet);
        else
            infoTweets.style.display = "none";
    });
}

function limpaResultado(){
    const infoLivro = document.querySelector("#info-livro");
    const infoTweets = document.querySelector("#info-tweets");
    const listaTweets = document.querySelector("#lista-tweets");
    
    infoLivro.style.display = "none";
    infoTweets.style.display = "none";
    listaTweets.innerHTML = '';

    const msgError = document.querySelector("#msg-erro"); 
    if(msgError)
        msgError.style.display = "none";
}