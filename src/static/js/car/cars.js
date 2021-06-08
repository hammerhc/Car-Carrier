var carTable = document.getElementById("carTable");

var cars = [
    {
        id: 1,
        name: "Test Car 1",
        model: "Test",
        price: 10000
    },
    {
        id: 2,
        name: "Test Car 2",
        model: "Test",
        price: 10000
    },
    {
        id: 3,
        name: "Test Car 3",
        model: "Test",
        price: 10000
    }
]

createCards();

function createCards() {
    for (var i = 0; i < cars.length; i++) {
        var card = `<div id="car${cars[i].id}" class="card" onclick="openCar(event)">
                        <img class="image">
                        <p>${cars[i].name} ${cars[i].model} ${cars[i].price}$</p>
                    </div>`

        carTable.innerHTML += card;
    }
}

function openCar(event) {
    var carId = event.target.id.replace("car", "");

    if (carId == "") {
        for (var i = 0; i < event.path.length; i++) {
            if (event.path[i].id.length > 0) {
                carId = event.path[i].id.replace("car", "");
                break;
            }
        }
    }

    navigate("/cars?id=" + carId);
}