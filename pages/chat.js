
import { useState } from 'react';

export default function Chat() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setResponse(data.reply);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>TAS.DAR GPT Chat</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          rows={4}
          cols={50}
          placeholder="Tulis mesej anda di sini..."
        />
        <br />
        <button type="submit">Hantar</button>
      </form>
      {response && (
        <div>
          <h3>Respon GPT:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}
