import { useEffect, useState } from "react";

const SHEET_ID = "1pAc8AlCdPFduk1cblYitu9fz3eg8_05OfFsQg2GF48I";
const API_KEY = "AIzaSyAFRrPi7543HhKRsSkID9F-H9oHVv5sm0k";
const RANGE = "Sheet1!A1:D";

export default function Leaderboard() {

  const [users, setUsers] = useState([]);

  function updateLeaderBoard(){
  fetch(`https://sheets.googleapis.com/v4/spreadsheets/${SHEET_ID}/values/${RANGE}?key=${API_KEY}`)
    .then(res => res.json())      
    .then(data => {               
      if (data.values) {
        const formatted = data.values.slice(1).map(row => ({
          name: row[0],
          score: row[1],
        }));
        setUsers(formatted);      
      }
    })
    .catch(err => console.error(err));
}


 useEffect(() => {
  setInterval(updateLeaderBoard, 5000);
}, []);


  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 via-gray-800 to-gray-900 text-white flex flex-col items-center p-6">
      <h1 className="text-4xl font-bold mt-6 mb-8 text-yellow-400 tracking-wide">
        🏆 Leaderboard
      </h1>

      <div className="w-full max-w-2xl flex flex-col space-y-4">
        {users.map((user, index) => (
          <div
            key={index}
            className={`flex justify-between items-center px-6 py-4 rounded-2xl shadow-md transition-all duration-300 
            ${index === 0 ? "bg-yellow-500 text-black scale-105" : "bg-gray-700 hover:bg-gray-600"}
            `}
          >
            <div className="flex items-center space-x-4">
              <span className="text-2xl font-bold text-yellow-300">
                #{index + 1}
              </span>
              <span className="text-lg font-semibold">{user.name}</span>
            </div>
            <span className="text-xl font-bold">{user.score}</span>
          </div>
        ))}
      </div>

    </div>
  );
  
}
