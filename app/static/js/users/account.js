// Input Validation Erros
const form = document.getElementById('accountForm')
const fname = document.getElementById('fname')
const lname = document.getElementById('lname')
const uname = document.getElementById('uname')
const email = document.getElementById('email')
const pw_current = document.getElementById('pw_current')
const pw_new = document.getElementById('pw_new')
const pw_confirm = document.getElementById('pw_confirm')

form.addEventListener('submit', (e) => {
    let messages = []

    // Email:
    if (!email.value === '' || !email.value == null) {
        if (!email.value.includes('@') || !email.value.includes('.')) {
            messages.push('Not a valid Email')
            messages.push("Email has to include ' @ ' and ' . '")
        }
    }

    // Password:
    if (!pw_new.value === '' || !pw_new.value == null) {
        if (pw_new.value.length <= 6) {
            messages.push('Password must be longer than 6 characters')
        } else if (pw_new.value.length >= 30) {
            messages.push('Password must be less than 30 characters')
        }
    }

    // Password Confirm:
    if (pw_new.value != pw_confirm.value) {
        messages.push('Passwords do not match.')
    }

    // Error Messages:
    if (messages.length > 0) {
        e.preventDefault();
        clearPreviousErrors();
        AddNewErrors(messages);
    }
})

// Functions:
let clearPreviousErrors = () => document.querySelectorAll('.generatedErrors').forEach( (e) => e.remove());

let AddNewErrors = (messages) => {
    for (let i = 0; i < messages.length; i++) {
        const newP = document.createElement("p");
        newP.setAttribute("class", "generatedErrors")
        newP.innerText = messages[i];
        document.getElementById("accountForm").appendChild(newP);
    }
}


// Delete User with deleteButton
const deleteButton = document.querySelector(".delete");

deleteButton.addEventListener("click", () => {
    form.addEventListener('submit', (e) => {
        e.preventDefault()
    });
    window.location.replace('/deleteuser')
});