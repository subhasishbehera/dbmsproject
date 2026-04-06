import { useState } from "react";
import API from "../api";

function BookAppointment() {
  const [form, setForm] = useState({});

  const submit = async () => {
    const res = await API.post("/appointment", form);
    alert(JSON.stringify(res.data));
  };

  return (
    <div>
      <h2>Book Appointment</h2>

      <input placeholder="Patient ID"
        onChange={(e)=>setForm({...form,patient_id:e.target.value})}/>

      <input placeholder="Doctor ID"
        onChange={(e)=>setForm({...form,doctor_id:e.target.value})}/>

      <input type="datetime-local"
        onChange={(e)=>setForm({...form,time:e.target.value})}/>

      <button onClick={submit}>Book</button>
    </div>
  );
}

export default BookAppointment;