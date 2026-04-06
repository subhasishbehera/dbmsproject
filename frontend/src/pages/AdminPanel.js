import { useEffect, useState } from "react";
import API from "../api";

function AdminPanel() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    API.get("/logs").then(res => setLogs(res.data));
  }, []);

  return (
    <div>
      <h2>System Logs</h2>

      {logs.map(log => (
        <div key={log.id}>
          {log.action} - {log.details} - {log.timestamp}
        </div>
      ))}
    </div>
  );
}

export default AdminPanel;