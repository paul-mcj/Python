let socketio = io();

const messages = document.getElementById("messages");

const createMessage = (name, msg) => {
	const content = `
     <div class="text">
        <span>
            <strong>${name}</strong>: ${msg}
        </span>
        <span class="muted">
            ${new Date().toLocaleString()}
        </span>
    </div>
    `;
	messages.innerHTML += content;
};

const sendMessage = () => {
	const userMessage = document.getElementById("message");

	if (userMessage.value === "") return;

	// special event
	socketio.emit("message", { data: userMessage.value });
	userMessage.value = ""; // clear out input
};

// listen for message event
socketio.on("message", (data) => {
	createMessage(data.name, data.message);
});
