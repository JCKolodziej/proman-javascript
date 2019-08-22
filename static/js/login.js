export function loginProcess() {
    let loginForm = document.getElementById('loginForm');
    let login = document.getElementById('defaultForm-username').value;
    let password = document.getElementById('defaultForm-pass').value;
    loginForm.addEventListener("submit", function (event) {
        event.cancelable = true;
        event.preventDefault();
        console.log(login, password);
        validationChecker(login, password)
    });
}


function validationChecker(login, password) {
    let validationData = {
        login: login,
        password: password
    };
    fetch('/login_process', {
        method: 'POST',
        mode: "same-origin",
        credentials: "same-origin",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(validationData)

    })
        .then(response => response.json())
        .then(validation => {
            if (validation.success === true) {
                window.location.replace('/')
            } else {
                let alertBar = document.getElementById('invalidCredentials');
                alertBar.style.display = 'block'
            }
        })
}