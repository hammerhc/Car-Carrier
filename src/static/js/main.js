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

setEvents();

function navigate(path) {
    document.location.pathname = path;
}

function setEvents() {
    navButtonHome.addEventListener("click", function () { navigate("/") });
    navButtonCars.addEventListener("click", function () { navigate("/cars") });
    navButtonOrders.addEventListener("click", function () { navigate("/orders") });
    navButtonTickets.addEventListener("click", function () { navigate("/tickets") });
    navButtonAdmin.addEventListener("click", function () { navigate("/admin") });

    profileButton.addEventListener("click", function () { navigate("/account") });
}