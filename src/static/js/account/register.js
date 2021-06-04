if (loggedIn) {
    navigate("/");
}

function createAccount(event) {
    var errorMessage = document.getElementById("errorMessage");
    errorMessage.innerHTML = "";

    var username = document.getElementById("inputUsername");
    var password = document.getElementById("inputPassword");
    var password2 = document.getElementById("inputPassword2");

    var result = checkCredentials(username, password, password2);

    if (result.error) {
        loggedIn = false;
        errorMessage.innerHTML = result.message;
    } else {
        sessionStorage.username = username.value;
        loggedIn = true;
        navigate("/");
    }
}

function checkCredentials(username, password, password2) {
    if (username.value.length <= 0) {
        return {
            error: true, 
            message: "Please enter a username."
        }
    }

    if (password.value.length <= 0) {
        return {
            error: true, 
            message: "Please enter a Password."
        }
    }

    if (password2.value.length <= 0) {
        return {
            error: true, 
            message: "Please confirm your password."
        }
    }

    if (password.value != password2.value) {
        return {
            error: true, 
            message: "Passwords dont match."
        }
    }

    return false;
}