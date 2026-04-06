import { useEffect, useState } from "react";
import API from "../api";

function Dashboard() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    API.get("/appointments").then(res => setAppointments(res.data));
  }, []);

  return (
    <div className="container">
      <h2>Appointments</h2>

      {appointments.map(a => (
        <div className="card" key={a.id}>
          Patient ID: {a.patient_id} <br/>
          Doctor ID: {a.doctor_id} <br/>
          Time: {a.time}
        </div>
      ))}
    </div>
  );
}

export default Dashboard;