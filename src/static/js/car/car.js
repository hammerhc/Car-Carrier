var url = new URL(window.location);
var params = new URLSearchParams(url.search);

var carId = params.get("id");

var carName = document.getElementById("carName");
carName.innerHTML += carId;

function back() {
    navigate("/cars");
}

function buyCar() {
    console.log("Buy car " + carId);
}