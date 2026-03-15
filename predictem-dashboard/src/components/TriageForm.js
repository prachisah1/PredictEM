import React, { useState } from "react";

function TriageForm() {

  const [form, setForm] = useState({
    heart_rate: "",
    blood_pressure: "",
    oxygen_level: "",
    injury_severity: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {

    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    const response = await fetch("http://127.0.0.1:8001/triage", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });

    const data = await response.json();

    setResult(data.triage_category);
  };

  return (

    <div>

      <h2>Triage Prediction</h2>

      <form onSubmit={handleSubmit}>

        <input name="heart_rate" placeholder="Heart Rate" onChange={handleChange} />

        <input name="blood_pressure" placeholder="Blood Pressure" onChange={handleChange} />

        <input name="oxygen_level" placeholder="Oxygen Level" onChange={handleChange} />

        <input name="injury_severity" placeholder="Injury Severity" onChange={handleChange} />

        <button type="submit">Predict</button>

      </form>

      {result && <h3>Triage Category: {result}</h3>}

    </div>
  );
}

export default TriageForm;