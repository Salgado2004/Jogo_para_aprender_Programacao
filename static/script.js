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
    var elemento = document.getElementById(data).cloneNode(true);
    ev.target.appendChild(elemento);
    var verifica = elemento.children;
    for (var i=0; verifica[i]; i++) {
        var nome = verifica[i].getAttribute('name');
        verifica[i].setAttribute('name', nome+ordem);
        var esconde = verifica[i].getAttribute('hidden');
        if(esconde != null){ 
            verifica[i].setAttribute('value', ordem);
        }
    }
}

var contador = 10;
function NovaDiv() {
    var area = document.getElementById("areaBlocos").innerHTML;
    var novaArea = area + '<div class="dropin" id="NovaDiv'+contador+'" ondrop="drop(event, '+contador+')" ondragover="allowDrop(event)"></div>';
    contador = contador + 1;
    document.getElementById("areaBlocos").innerHTML = novaArea;
}
