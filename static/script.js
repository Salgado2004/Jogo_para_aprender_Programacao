function allowDrop(ev) {
    ev.preventDefault();
  }
  
  function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
  }
  
 function drop(ev, valor) {
    ev.preventDefault();
    ordem = valor;
    var data = ev.dataTransfer.getData("text");
    var template = document.getElementById(data).getAttribute('alt');
    if (template == 'template' ){
      var elemento = document.getElementById(data).cloneNode(true);
      var id = document.getElementById(data).getAttribute('id').split(".");
      ev.target.appendChild(elemento);
      elemento.setAttribute('id', id[0]+"."+ordem);
      elemento.setAttribute('alt', ' ');
      var img = document.createElement("img");
      img.setAttribute('src', '../static/img/deletar.png');
      img.setAttribute('onclick', 'apagar("'+id[0]+'.'+ordem+'")');
      elemento.appendChild(img);
    } else{
      var elemento = document.getElementById(data);
      ev.target.appendChild(elemento);
    }
    var verifica = elemento.children;
    for (var i=0; verifica[i]; i++) {
        var nome = verifica[i].getAttribute('name').split(".");
        verifica[i].setAttribute('name', nome[0]+"."+ordem);
        var esconde = verifica[i].getAttribute('hidden');
        if(esconde != null){ 
            verifica[i].setAttribute('value', ordem);
        }
    }
}

var contador = 6;
function NovaDiv() {
    var area = document.getElementById("areaBlocos").innerHTML;
    var novaArea = area + '<div class="dropin" id="NovaDiv'+contador+'" ondrop="drop(event, '+contador+')" ondragover="allowDrop(event)"></div>';
    contador = contador + 1;
    document.getElementById("areaBlocos").innerHTML = novaArea;
}

function apagar(id){
  var elemento = document.getElementById(id);
  elemento.remove();
}
