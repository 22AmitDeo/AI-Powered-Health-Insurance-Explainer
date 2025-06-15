// chat.js
document.getElementById("chatForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const queryInput = document.getElementById("userQuery");
    const responseBox = document.getElementById("chatResponse");
    const question = queryInput.value.trim();

    if (!question) return;

    responseBox.innerHTML = "Thinking...";

    const formData = new FormData();
    formData.append("query", question);

    try {
        const response = await fetch("http://localhost:8000/chat", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();
        responseBox.innerHTML = `<strong>AI:</strong> ${result.response}`;
    } catch (err) {
        responseBox.innerHTML = "❌ Failed to get a response.";
        console.error(err);
    }
});
