const email = document.getElementById('email')
const password = document.getElementById('password')
const pw_confirm = document.getElementById('pw_confirm')
const form = document.getElementById('signupForm')

form.addEventListener('submit', (e) => {
    let messages = []
    if (email.value === '' || email.value == null) {
        messages.push('Email is required')
    } else if (!email.value.includes('@') || !email.value.includes('.')) {
        messages.push('Not a valid Email')
        messages.push("Email has to include ' @ ' and at least one ' . '")
    }

    if (password.value === '' || email.value == null) {
        messages.push('Password is required')
    } else if (password.value.length <= 6) {
        messages.push('Password must be longer than 6 characters')
    } else if (password.value.length >= 30) {
        messages.push('Password must be less than 30 characters')
    }

    if (password.value != pw_confirm.value) {
        messages.push('Passwords does not match.')
    }

    if (messages.length > 0) {
        e.preventDefault();
        clearPreviousErrors();
        AddNewErrors(messages);
    }
})

let clearPreviousErrors = () => document.querySelectorAll('.generatedErrors').forEach(e => e.remove());

let AddNewErrors = (messages) => {
    for (let i = 0; i < messages.length; i++) {
        const newP = document.createElement("p");
        newP.setAttribute("class", "generatedErrors")
        newP.innerText = messages[i];
        document.getElementById("signupForm").appendChild(newP);
    }
}
