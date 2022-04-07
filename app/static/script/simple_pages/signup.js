let email = document.getElementById('email')
let password = document.getElementById('password')
let form = document.getElementById('signupForm')
let errorElement = document.getElementById('error')

form.addEventListener('submit', (e) => {
    let messages = []
    if (email.value === '' || email.value == null) {
        messages.push('Email is required')
    } 
    
    if (!email.value.includes('@')) {
        messages.push('Not a valid Email')
    }

    if (password.value.length <= 6) {
        messages.push('Password must be longer than 6 characters')
    }

    if (password.value.length >= 30) {
        messages.push('Password must be less than 30 characters')
    }

    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
})


// function submitForm()
// {
//     if(getElementById("email") == null || getElementById("password") == null) { 
//         let error = "Please fill out all input fields to sign up!";
//     }
//     else {
//         alert("validations passed");
//         getElementById("signupForm").submit();
//     }
// }

// getElementById("submitButton").addEventListener("click", submitForm());

