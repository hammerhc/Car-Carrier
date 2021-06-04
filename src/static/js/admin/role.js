var url = new URL(window.location);
var params = new URLSearchParams(url.search);

var roleId = params.get("id");

function cancel() {
    navigate("/roles");
}

function save() {
    console.log("Saving");
}