const bookContainer = document.querySelector('.book-container')
bookContainer.addEventListener('click', clickHandler)

function clickHandler (event) {
  const target = event.target.closest('.click-fav')
  const child = target.children[0]
  if (child.classList.contains('non-favorite')) {
    target.innerHTML = "<i class='fas fa-star favorite'></i>"
  }
  else {
    target.innerHTML = "<i class='far fa-star non-favorite'></i>"
  }
  return fetch(`/favorite/${target.dataset.id}`)
    .then(response => { })
}
