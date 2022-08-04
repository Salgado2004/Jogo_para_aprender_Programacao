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
    ev.target.appendChild(document.getElementById(data));
    var verifica =document.getElementById(data).children;
    for (var i=0; verifica[i]; i++) {
        var classe = verifica[i].getAttribute('hidden');
        if(classe != null){ 
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