document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("userInput");
    const output = document.getElementById("chatOutput");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();
        const userMessage = input.value.trim();
        if (!userMessage) return;

        const userText = document.createElement("p");
        userText.innerHTML = <strong>Kau:</strong> ${userMessage};
        output.appendChild(userText);

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage })
            });

            const data = await response.json();
            const replyElement = document.createElement("p");
            replyElement.innerHTML = <strong>TAS.DAR:</strong> ${data.reply};
            output.appendChild(replyElement);
        } catch (error) {
            const errorMsg = document.createElement("p");
            errorMsg.style.color = "red";
            errorMsg.textContent = "⚠ Gagal hubungi GPT.";
            output.appendChild(errorMsg);
        }

        input.value = "";
        input.focus();
    });
});
