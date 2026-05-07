import { useState } from "react";
import API from "../services/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    const res = await API.post("/auth/login", { email, password });
    localStorage.setItem("token", res.data.access_token);
    window.location.href = "/formations";
  };

  return (
    <div>
      <h2>TTAD Login</h2>
      <input onChange={e => setEmail(e.target.value)} placeholder="Email" />
      <input onChange={e => setPassword(e.target.value)} type="password" />
      <button onClick={login}>Login</button>
    </div>
  );
}