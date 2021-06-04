var orderTable = document.getElementById("orderTable");

var orders = [
    {
        id: 1,
        car: "Test Car 1",
        date: "2021.01.01",
        price: 10000
    },
    {
        id: 2,
        car: "Test Car 2",
        date: "2021.01.02",
        price: 10000
    },
    {
        id: 3,
        car: "Test Car 3",
        date: "2021.01.03",
        price: 10000
    }
]

createCards();

function createCards() {
    for (var i = 0; i < orders.length; i++) {
        var row = `<tr>
                        <td>${orders[i].id}</td>
                        <td>${orders[i].car}</td>
                        <td>${orders[i].date}</td>
                        <td>${orders[i].price}$</td>
                        <td><button id="cancelOrder${orders[i].id}" onclick="cancelOrder(event)">Cancel Order</button></td>
                    </tr>`

        orderTable.innerHTML += row;
    }
}

function cancelOrder(event) {
    var orderId = event.target.id.replace("cancelOrder", "");
}