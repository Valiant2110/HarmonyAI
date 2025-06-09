
import React, { useState } from 'react';

const BACKEND_URL = 'http://localhost:8080';

export default function App() {
  const [playlistPrompt, setPlaylistPrompt] = useState('');
  const [playlist, setPlaylist] = useState([]);
  const [audioFile, setAudioFile] = useState(null);
  const [moodResult, setMoodResult] = useState(null);
  const [theme, setTheme] = useState('');
  const [mood, setMood] = useState('');
  const [lyrics, setLyrics] = useState('');
  const [generatedMelody, setGeneratedMelody] = useState(null);

  const generatePlaylist = async () => {
    const res = await fetch(`${BACKEND_URL}/generate_playlist/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: playlistPrompt }),
    });
    const data = await res.json();
    setPlaylist(data.playlist || []);
  };

  const analyzeMood = async () => {
    const formData = new FormData();
    formData.append('file', audioFile);

    const res = await fetch(`${BACKEND_URL}/analyze_mood/`, {
      method: 'POST',
      body: formData,
    });
    const data = await res.json();
    setMoodResult(data);
  };

  const generateLyrics = async () => {
    const res = await fetch(`${BACKEND_URL}/generate_lyrics/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ theme, mood }),
    });
    const data = await res.json();
    setLyrics(data.lyrics || '');
  };

  const generateMelody = async () => {
    const res = await fetch(`${BACKEND_URL}/generate_melody/?mood=${encodeURIComponent(mood)}`, {
      method: 'POST',
    });
    const data = await res.json();
    if (data.melody_url) {
      setGeneratedMelody(`${BACKEND_URL}${data.melody_url}`);
    }
  };

  return (
    <div className="min-h-screen p-6 bg-gradient-to-b from-gray-900 via-black to-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-8 text-center">🎵 HarmonyAI 🎶</h1>

      <section className="mb-8">
        <h2 className="text-2xl mb-2">Generate Playlist</h2>
        <input
          type="text"
          className="w-full p-2 rounded bg-gray-800 border border-gray-700 mb-2"
          value={playlistPrompt}
          onChange={(e) => setPlaylistPrompt(e.target.value)}
          placeholder="Describe your mood or activity"
        />
        <button onClick={generatePlaylist} className="bg-blue-600 px-4 py-2 rounded hover:bg-blue-700">
          Generate Playlist
        </button>
        <ul className="mt-4 list-disc list-inside">
          {playlist.map((song, i) => (
            <li key={i}>{song}</li>
          ))}
        </ul>
      </section>

      <section className="mb-8">
        <h2 className="text-2xl mb-2">Analyze Mood from Audio</h2>
        <input
          type="file"
          accept="audio/*"
          onChange={(e) => setAudioFile(e.target.files[0])}
          className="mb-2"
        />
        <button onClick={analyzeMood} className="bg-green-600 px-4 py-2 rounded hover:bg-green-700">
          Analyze Mood
        </button>
        {moodResult && (
          <div className="mt-4">
            <p><strong>Mood:</strong> {moodResult.mood}</p>
            <p><strong>Description:</strong> {moodResult.description}</p>
          </div>
        )}
      </section>

      <section className="mb-8">
        <h2 className="text-2xl mb-2">Generate Lyrics</h2>
        <input
          type="text"
          placeholder="Theme"
          className="w-full p-2 rounded bg-gray-800 border border-gray-700 mb-2"
          value={theme}
          onChange={(e) => setTheme(e.target.value)}
        />
        <input
          type="text"
          placeholder="Mood"
          className="w-full p-2 rounded bg-gray-800 border border-gray-700 mb-2"
          value={mood}
          onChange={(e) => setMood(e.target.value)}
        />
        <button onClick={generateLyrics} className="bg-purple-600 px-4 py-2 rounded hover:bg-purple-700">
          Generate Lyrics
        </button>
        <div className="mt-4 whitespace-pre-wrap">{lyrics}</div>
      </section>

      <section className="mb-8">
        <h2 className="text-2xl mb-2">Generate Melody</h2>
        <button onClick={generateMelody} className="bg-pink-600 px-4 py-2 rounded hover:bg-pink-700">
          Generate Melody
        </button>
        {generatedMelody && (
          <div className="mt-4">
            <audio controls src={generatedMelody} className="w-full" />
          </div>
        )}
      </section>
    </div>
  );
}
