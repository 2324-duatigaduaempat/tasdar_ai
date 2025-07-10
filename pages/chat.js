import { useState } from 'react';

export default function Chatboard() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const sendMessage = async () => {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    setResponse(data.reply);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Chatboard TAS.DAR</h1>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        rows={4}
        cols={50}
        placeholder="Taip mesej di sini..."
      />
      <br />
      <button onClick={sendMessage}>Hantar</button>
      <div style={{ marginTop: '2rem', whiteSpace: 'pre-wrap' }}>
        <strong>Jawapan AI:</strong>
        <p>{response}</p>
      </div>
    </div>
  );
}
