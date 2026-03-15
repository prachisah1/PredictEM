import React, { useState } from "react";

function Dispatch() {

  const [hospital, setHospital] = useState(null);

  const dispatchAmbulance = async () => {

    const response = await fetch("http://127.0.0.1:8001/dispatch-ambulance");

    const data = await response.json();

    setHospital(data.nearest_hospital);
  };

  return (

    <div>

      <h2>Ambulance Dispatch</h2>

      <button onClick={dispatchAmbulance}>
        Find Nearest Hospital
      </button>

      {hospital && <h3>Nearest Hospital: {hospital}</h3>}

    </div>
  );
}

export default Dispatch;