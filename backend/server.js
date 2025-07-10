const express = require('express');
const app = express();
app.use(express.json());
app.post('/api/chat', (req, res) => {
  const message = req.body.message;
  res.json({ reply: "Ini jawapan AI kepada: " + message });
});
app.listen(3001, () => console.log('TAS.DAR API ready'));
