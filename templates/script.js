
async function sendMessage() {
    const message = document.getElementById('userInput').value;
    const responseDiv = document.getElementById('response');
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        responseDiv.innerText = data.reply || data.error;
    } catch (err) {
        responseDiv.innerText = "Ralat sambungan.";
    }
}
