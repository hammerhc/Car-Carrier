var loggedIn = false;

if (sessionStorage.username) {
    if (sessionStorage.username.length > 0) {
        loggedIn = true;
    }
}

var navButtonHome = document.getElementById("navButtonHome");
var navButtonCars = document.getElementById("navButtonCars");
var navButtonOrders = document.getElementById("navButtonOrders");
var navButtonTickets = document.getElementById("navButtonTickets");
var navButtonAdmin = document.getElementById("navButtonAdmin");

var profileButton = document.getElementById("profileButton");

var registerButton = document.getElementById("registerButton");
var loginButton = document.getElementById("loginButton");
var accountButton = document.getElementById("accountButton");
var logoutButton = document.getElementById("logoutButton");

setEvents();

function navigate(path) {
    window.location = location.protocol + "//" + location.host + path;
}

function setEvents() {
    navButtonHome.addEventListener("click", function () { navigate("/") });
    navButtonCars.addEventListener("click", function () { navigate("/cars") });
    navButtonOrders.addEventListener("click", function () { navigate("/orders") });
    navButtonTickets.addEventListener("click", function () { navigate("/tickets") });
    navButtonAdmin.addEventListener("click", function () { navigate("/users") });

    profileButton.addEventListener("click", dropdown);

    registerButton.addEventListener("click", function () { navigate("/register") });
    loginButton.addEventListener("click", function () { navigate("/login") });
    accountButton.addEventListener("click", function () { navigate("/account") });
    logoutButton.addEventListener("click", logout);
}

function dropdown() {
    if (loggedIn) {
        document.getElementById("userContainer").classList.toggle("show");
    } else {
        document.getElementById("guestContainer").classList.toggle("show");
    }
}

function logout() {
    navigate("/");

    if (sessionStorage.username) {
        sessionStorage.removeItem("username");
        loggedIn = false;
    }
}

window.onclick = function (event) {
    if (!event.target.matches('.dropButton')) {
        var dropdowns = document.getElementsByClassName("dropdownContent");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}