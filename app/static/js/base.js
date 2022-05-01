const flashedMessage = document.querySelector('.flashed')
const removeButton = document.querySelector('.remove_flashed')

if (removeButton) {
    removeButton.addEventListener('click', (e) => {
        flashedMessage.remove()
    });
}
