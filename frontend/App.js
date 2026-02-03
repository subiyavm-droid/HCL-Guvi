import React, { useEffect, useState } from "react";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [businessIds, setBusinessIds] = useState([]);
  const [selectedId, setSelectedId] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(`${API_BASE}/business_ids`)
      .then(res => res.json())
      .then(data => setBusinessIds(data))
      .catch(err => {
        console.error(err);
        setError("Backend not reachable. Is FastAPI running?");
      });
  }, []);

  const analyze = () => {
    fetch(`${API_BASE}/analyze/${selectedId}`)
      .then(res => res.json())
      .then(data => setResult(data))
      .catch(err => {
        console.error(err);
        setError("Backend not reachable. Is FastAPI running?");
      });
  };

  return (
    <div style={{ textAlign: "center", marginTop: "80px" }}>
      <h1>SME Financial Health Assessment Platform</h1>
      <p>Analyze SME financial risk in real time</p>

      <select onChange={e => setSelectedId(e.target.value)}>
        <option>Select Business ID</option>
        {businessIds.map(id => (
          <option key={id} value={id}>{id}</option>
        ))}
      </select>

      <br /><br />
      <button onClick={analyze}>Analyze SME</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h3>Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
