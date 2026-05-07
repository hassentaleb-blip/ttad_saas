import React, { useState, useEffect } from "react";

export default function Formations() {
  const [formations, setFormations] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");

  // LOAD
  const fetchFormations = async () => {
    const res = await fetch("http://localhost:5000/api/formations");
    const data = await res.json();
    setFormations(data);
  };

  useEffect(() => {
    fetchFormations();
  }, []);

  // ADD
  const addFormation = async () => {
    await fetch("http://localhost:5000/api/formations/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ title, description, price })
    });

    fetchFormations();
  };

  // DELETE
  const deleteFormation = async (id) => {
    await fetch(`http://localhost:5000/api/formations/${id}`, {
      method: "DELETE"
    });

    fetchFormations();
  };

  return (
    <div>
      <h1>TTAD Formations</h1>

      <input placeholder="Title" onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="Description" onChange={(e) => setDescription(e.target.value)} />
      <input placeholder="Price" onChange={(e) => setPrice(e.target.value)} />

      <button onClick={addFormation}>Add</button>

      <ul>
        {formations.map((f) => (
          <li key={f.id}>
            {f.title} - {f.price} TND
            <button onClick={() => deleteFormation(f.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}