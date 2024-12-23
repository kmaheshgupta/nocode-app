document.addEventListener("DOMContentLoaded", () => {
  const chatIcon = document.createElement("i");
  chatIcon.className = "fas fa-comments chat-icon";
  chatIcon.onclick = toggleChat;
  document.body.appendChild(chatIcon);

  const chatWindow = document.createElement("div");
  chatWindow.className = "chat-window";
  chatWindow.id = "chat-window";
  chatWindow.innerHTML = `
    <div class="chat-header">
      Chat with AI Bot
      <i class="fas fa-times close-btn" onclick="toggleChat()"></i>
    </div>
    <div class="chat-body" id="chat-body"></div>
    <div class="chat-footer">
      <input type="text" id="chat-input" placeholder="Type a message..." />
      <button onclick="sendMessage()"><i class="fas fa-paper-plane"></i></button>
    </div>
  `;
  document.body.appendChild(chatWindow);
});

function toggleChat() {
  const chatWindow = document.getElementById("chat-window");
  chatWindow.style.display =
    chatWindow.style.display === "none" || chatWindow.style.display === ""
      ? "flex"
      : "none";
}

function sendMessage() {
  const chatInput = document.getElementById("chat-input");
  const chatBody = document.getElementById("chat-body");
  const message = chatInput.value.trim();
  if (message) {
    const customerMessage = document.createElement("div");
    customerMessage.className = "chat-message customer";
    customerMessage.innerHTML = `<span class="role">Customer:</span> <span class="text">${message}</span>`;
    chatBody.appendChild(customerMessage);
    chatInput.value = "";

    fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    })
      .then((response) => response.json())
      .then((data) => {
        const botMessage = document.createElement("div");
        botMessage.className = "chat-message ai-bot";
        botMessage.innerHTML = `<span class="role">AI Bot:</span> <span class="text">${data.response}</span>`;
        chatBody.appendChild(botMessage);
        chatBody.scrollTop = chatBody.scrollHeight;
      });
  }
}
