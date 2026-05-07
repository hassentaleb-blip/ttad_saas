import { useEffect, useState } from "react";
import API from "../services/api";

export default function Formations() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("/formations").then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h1>Formations TTAD</h1>
      {data.map(f => (
        <div key={f.id}>
          {f.title} - {f.price} DT
        </div>
      ))}
    </div>
  );
}