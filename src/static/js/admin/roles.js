var rolesTable = document.getElementById("rolesTable");

var rolesArray = [
    {
        id: 1,
        name: "Customer"
    },
    {
        id: 2,
        name: "Agent"
    },
    {
        id: 3,
        name: "Admin"
    }
]

createRows();

function createRows() {
    for (var i = 0; i < rolesArray.length; i++) {
        var row = `<tr>
                        <td>${rolesArray[i].id}</td>
                        <td>${rolesArray[i].name}</td>
                        <td><button id="editRole${rolesArray[i].id}" onclick="editRole(event)">Edit Role</button></td>
                        <td><button id="removeRole${rolesArray[i].id}" onclick="removeRole(event)">Remove Role</button></td>
                    </tr>`

        rolesTable.innerHTML += row;
    }
}

function editRole(event) {
    var roleId = event.target.id.replace("editRole", "");

    navigate("/roles?id=" + roleId);
}

function removeRole(event) {
    var roleId = event.target.id.replace("removeRole", "");
}

function users() {
    navigate("/users");
}

function roles() {
    navigate("/roles");
}