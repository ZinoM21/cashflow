const deleteButton = document.querySelector(".delete");
const form = document.getElementById('accountForm')

deleteButton.addEventListener("click", () => {
    form.addEventListener('submit', (e) => {
        e.preventDefault()
    });
    window.location.replace('/deleteuser')
});