var navButtonHome = document.getElementById("navButtonHome");
var navButtonCars = document.getElementById("navButtonCars");
var navButtonOrders = document.getElementById("navButtonOrders");
var navButtonTickets = document.getElementById("navButtonTickets");
var navButtonAdmin = document.getElementById("navButtonAdmin");

var profileButtonHome = document.getElementById("profileButtonHome");

var buyButtonHome = document.getElementById("buyButtonHome");

setEvents();

function navigate(path) {
    document.location.pathname = path;
}

function setEvents() {
    navButtonHome.addEventListener("click", function() {navigate("/")});
    navButtonCars.addEventListener("click", function() {navigate("/cars")});
    navButtonOrders.addEventListener("click", function() {navigate("/orders")});
    navButtonTickets.addEventListener("click", function() {navigate("/tickets")});
    navButtonAdmin.addEventListener("click", function() {navigate("/admin")});
}