var ticketTable = document.getElementById("ticketTable");

var tickets = [
    {
        id: 1,
        title: "Test Ticket 1",
        owner: 1,
        createdAt: "2021.01.01",
        updatedAt: "2021.01.01 10:00"
    },
    {
        id: 2,
        title: "Test Ticket 2",
        owner: 1,
        createdAt: "2021.01.02",
        updatedAt: "2021.01.02 10:00"
    },
    {
        id: 3,
        title: "Test Ticket 3",
        owner: 1,
        createdAt: "2021.01.03",
        updatedAt: "2021.01.03 10:00"
    }
]

createRows();

function createRows() {
    for (var i = 0; i < tickets.length; i++) {
        var row = `<tr>
                        <td>${tickets[i].id}</td>
                        <td>${tickets[i].title}</td>
                        <td>${tickets[i].owner}</td>
                        <td>${tickets[i].createdAt}</td>
                        <td>${tickets[i].updatedAt}</td>
                        <td><button id="editTicket${tickets[i].id}" onclick="editTicket(event)">Edit Ticket</button></td>
                        <td><button id="closeTicket${tickets[i].id}" onclick="closeTicket(event)">Close Ticket</button></td>
                    </tr>`

        ticketTable.innerHTML += row;
    }
}

function editTicket(event) {
    var ticketId = event.target.id.replace("editTicket", "");

    navigate("/tickets?id=" + ticketId);
    
}

function closeTicket(event) {
    var ticketId = event.target.id.replace("closeTicket", "");
}