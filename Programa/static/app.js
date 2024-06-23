var aumentar = document.getElementById('aumentar')
var diminuir = document.getElementById('diminuir')
var control = 0

aumentar = document.addEventListener('click', (e)=>{
  control++
  var text= document.getElementById('qtd').innerHTML = control
})
