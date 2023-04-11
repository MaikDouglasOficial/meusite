// seleciona o menu lateral
const menuLateral = document.getElementById("menu-lateral");

// adiciona um listener para o evento 'mousedown'
menuLateral.addEventListener("mousedown", function(event) {
  // previne que o comportamento padrão ocorra
  event.preventDefault();

  // armazena a posição inicial do mouse
  const startX = event.clientX;
  const startY = event.clientY;

  // armazena a posição inicial do menu
  const initialX = menuLateral.offsetLeft;
  const initialY = menuLateral.offsetTop;

  // adiciona um listener para o evento 'mousemove'
  document.addEventListener("mousemove", moveMenu);

  // adiciona um listener para o evento 'mouseup'
  document.addEventListener("mouseup", removeListeners);

  // função para mover o menu
  function moveMenu(event) {
    // calcula a nova posição do menu baseado no movimento do mouse
    const newX = initialX + event.clientX - startX;
    const newY = initialY + event.clientY - startY;

    // atualiza a posição do menu
    menuLateral.style.left = `${newX}px`;
    menuLateral.style.top = `${newY}px`;

    // salva a posição do menu no Local Storage
    localStorage.setItem("menuPositionX", newX);
    localStorage.setItem("menuPositionY", newY);
  }

  // função para remover os listeners dos eventos 'mousemove' e 'mouseup'
  function removeListeners() {
    document.removeEventListener("mousemove", moveMenu);
    document.removeEventListener("mouseup", removeListeners);
  }
});

// adiciona um listener para o evento 'beforeunload'
window.addEventListener("beforeunload", function() {
  // armazena a posição atual do menu no Local Storage
  localStorage.setItem("menuPositionX", menuLateral.offsetLeft);
  localStorage.setItem("menuPositionY", menuLateral.offsetTop);
});

// verifica se a posição do menu está armazenada no Local Storage
const menuPositionX = localStorage.getItem("menuPositionX");
const menuPositionY = localStorage.getItem("menuPositionY");

if (menuPositionX && menuPositionY) {
  // define a posição do menu para a posição armazenada no Local Storage
  menuLateral.style.left = `${menuPositionX}px`;
  menuLateral.style.top = `${menuPositionY}px`;
}
