document.addEventListener('DOMContentLoaded', function() {
  var funcao = document.querySelector('.content').getAttribute('data-funcao');

  document.querySelector('.content').addEventListener('click', function(event) {
      if (event.target.classList.contains('adicionar') || event.target.classList.contains('remover')) {
          var index = event.target.getAttribute('data-index');
          var qtdElement = document.getElementById('qtd-' + index);
          var currentQtd = parseInt(qtdElement.innerHTML);

          if (funcao === 'Retirada') {
              var retirarElement = document.getElementById('retirar-' + index);
              var currentRetirar = parseInt(retirarElement.innerHTML);

              if (event.target.classList.contains('adicionar')) {
                  if (currentRetirar < currentQtd) {
                      retirarElement.innerHTML = currentRetirar + 1;
                  }
              } else if (event.target.classList.contains('remover')) {
                  if (currentRetirar > 0) {
                      retirarElement.innerHTML = currentRetirar - 1;
                  }
              }
          } else {
              if (event.target.classList.contains('adicionar')) {
                  qtdElement.innerHTML = currentQtd + 1;
              } else if (event.target.classList.contains('remover')) {
                  if (currentQtd > 0) {
                      qtdElement.innerHTML = currentQtd - 1;
                  }
              }
          }
      }
  });
});
