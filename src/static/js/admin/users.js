var usersTable = document.getElementById("usersTable");

var users = [
    {
        id: 1,
        username: "Test User 1",
        role: "Customer"
    },
    {
        id: 2,
        username: "Test User 2",
        role: "Customer"
    },
    {
        id: 3,
        username: "Test User 3",
        role: "Customer"
    }
]

createRows();

function createRows() {
    for (var i = 0; i < users.length; i++) {
        var row = `<tr>
                        <td>${users[i].id}</td>
                        <td>${users[i].username}</td>
                        <td>${users[i].role}</td>
                        <td><button id="editUser${users[i].id}" onclick="editUser(event)">Edit User</button></td>
                        <td><button id="removeUser${users[i].id}" onclick="removeUser(event)">Remove User</button></td>
                    </tr>`

        usersTable.innerHTML += row;
    }
}

function editUser(event) {
    var userId = event.target.id.replace("editUser", "");

    navigate("/users?id=" + userId);
}

function removeUser(event) {
    var userId = event.target.id.replace("removeUser", "");
}

function users() {
    navigate("/users");
}

function roles() {
    navigate("/roles");
}