var url = new URL(window.location);
var params = new URLSearchParams(url.search);

var userId = params.get("id");

function cancel() {
    navigate("/users");
}

function save() {
    console.log("Saving");
}