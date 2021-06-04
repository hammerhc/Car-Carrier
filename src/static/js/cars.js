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
        var card = `<div class="card">
                        <img>
                        <div class="cardControls">
                            <span>${cars[i].price}$</span>
                            <button id="buyCar${cars[i].id}" class="buyButton" onclick="buyCar(event)">Buy</button>
                        </div>
                        <p>${cars[i].name} ${cars[i].model} ${cars[i].price}$</p>
                    </div>`

        carTable.innerHTML += card;
    }
}

function buyCar(event) {
    var carId = event.target.id.replace("buyCar", "");
}