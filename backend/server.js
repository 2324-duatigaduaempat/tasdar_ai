app.post('/api/chat', (req, res) => {
  const message = req.body.message;
  res.json({ reply: "Ini jawapan AI kepada: " + message });
});
