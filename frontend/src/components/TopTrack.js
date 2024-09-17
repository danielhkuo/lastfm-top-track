import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TopTrack = () => {
  const [track, setTrack] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTopTrack = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/top-track');
        setTrack(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch top track');
        setLoading(false);
      }
    };

    fetchTopTrack();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!track) return <div>No top track found for this month.</div>;

  return (
    <div className="top-track">
      <h1>My Top Track This Month</h1>
      <div className="track-info">
        <h2>{track.name}</h2>
        <p>by {track.artist}</p>
        <p>Played {track.playcount} times</p>
      </div>
    </div>
  );
};

export default TopTrack;