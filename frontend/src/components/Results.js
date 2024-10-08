// frontend/src/components/Results.js

import React from "react";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";
import "./Results.css"; // Import the CSS file

function Results({ results }) {
  if (!results.length) return null;

  // Map document IDs and their cosine similarity to the data array
  const data = results.map((item) => ({
    name: `Document ${item.doc_id}`, // Use Document ID here
    score: item.score,
  }));

  return (
    <div>
      <h2>Top Documents</h2>

      <div className="row">
        {results.map((item, index) => (
          <div className="col-12 mb-4" key={index}>
            <div className="card">
              <div className="card-header">
                <h5>Document {item.doc_id}</h5>
                <small>Score: {item.score.toFixed(4)}</small>
              </div>
              <div className="card-body">
                <p className="card-text">{item.document}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      <h2>Cosine Similarity Bar Chart</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="name" /> {/* Now displays Document IDs */}
          <YAxis domain={[0, 1]} />
          <Tooltip />
          <CartesianGrid stroke="#f5f5f5" />
          <Bar dataKey="score" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default Results;
