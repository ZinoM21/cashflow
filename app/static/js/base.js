const flashedMessage = document.querySelector('.flashed')
const removeButton = document.querySelector('.remove_flashed')

removeButton.addEventListener('click', (e) => {
    flashedMessage.remove()
});
