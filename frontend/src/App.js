// frontend/src/App.js

import React, { useState } from "react";
import axios from "axios";
import SearchBar from "./components/SearchBar";
import Results from "./components/Results";
import "./App.css"; // Import the CSS file

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query) return;
    setLoading(true);
    try {
      const response = await axios.post("/search", { query });
      setResults(response.data.results);
    } catch (error) {
      console.error("Error fetching search results:", error);
      alert("An error occurred while fetching results.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>LSA Search Engine</h1>
      <SearchBar
        query={query}
        setQuery={setQuery}
        handleSearch={handleSearch}
      />
      {loading ? (
        <div className="text-center">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      ) : (
        <Results results={results} />
      )}
    </div>
  );
}

export default App;
