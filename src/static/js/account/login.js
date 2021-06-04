if (loggedIn) {
    navigate("/");
}

function login(event) {
    var errorMessage = document.getElementById("errorMessage");
    errorMessage.innerHTML = "";

    var username = document.getElementById("inputUsername");
    var password = document.getElementById("inputPassword");

    var result = checkCredentials(username, password);

    if (result.error) {
        loggedIn = false;
        errorMessage.innerHTML = result.message;
    } else {
        sessionStorage.username = username.value;
        loggedIn = true;
        navigate("/");
    }
}

function checkCredentials(username, password) {
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

    return false;
}