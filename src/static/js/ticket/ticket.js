var url = new URL(window.location);
var params = new URLSearchParams(url.search);

var ticketId = params.get("id");

var messageContainer = document.getElementById("messageContainer");
var messageInput = document.getElementById("messageInput");

var ticketIdText = document.getElementById("ticketId");
var ticketTitleText = document.getElementById("ticketTitle");

ticketIdText.innerHTML += ticketId;
ticketTitleText.innerHTML += "Test Ticket " + ticketId;

function back() {
    navigate("/tickets");
}

function closeTicket() {
    back();
}

function sendMessage() {
    if (messageInput.value.length > 0) {
        messageContainer.innerHTML += createMessage(messageInput.value);
        messageInput.value = "";
        messageInput.focus();
    }
}

function createMessage(message) {
    return `<div class="message"><span>${message}</span></div>`
}