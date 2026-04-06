import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div>
      <Link to="/">Login</Link> | 
      <Link to="/dashboard">Dashboard</Link> | 
      <Link to="/admin">Admin</Link>
    </div>
  );
}

export default Navbar;