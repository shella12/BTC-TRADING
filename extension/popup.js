fetch("http://localhost:5000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    open: 67000,
    high: 67500,
    low: 66500,
    close: 67300,
    volume: 50
  })
})
  .then(res => res.json())
  .then(data => {
    document.getElementById("signal").textContent =
      data.prediction === 1 ? "BTC going UP ⬆️" : "BTC going DOWN ⬇️";
  });
