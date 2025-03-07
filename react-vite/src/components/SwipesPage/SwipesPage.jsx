import { useEffect, useState } from "react";
// import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import OpenModalButton from "../OpenModalButton";
import CharacterFormModal from "../CharacterFormModal/CharacterFormModal";
import "./SwipesPage.css"

export default function SwipesPage() {
  const [character, setCharacter] = useState(null);
  const [loading, setLoading] = useState(true);
  const [fluttering, setFluttering] = useState("");  // Add state to track fluttering direction

  // Fetch a random character
  const fetchCharacter = async () => {
    setLoading(true);
    try {
      const response = await fetch("/api/characters/random");
      if (!response.ok) throw new Error("Failed to fetch character");
      const data = await response.json();
      setCharacter(data);
    } catch (error) {
      console.error("Error fetching character:", error);
    } finally {
      setLoading(false);
    }
  };

  // Handle Like
  const handleLike = async () => {
    if (!character) return;
    try {
      const response = await fetch(`/api/characters/${character.id}/likes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // Ensure cookies are sent
      });

      if (!response.ok) {
        const data = await response.json();
        console.error(data.error_message);

        // If the user has liked all characters, show end message
        if (response.status === 400) {
          setCharacter(null); // This will trigger the "end" message
        }
        return;
      }

      // Successfully liked, trigger flutter to the right
      setFluttering("right");
      setTimeout(() => {
        setFluttering("");  // Reset flutter after animation
        fetchCharacter();   // Fetch next character
      }, 1500);  // Match the duration of the animation
    } catch (error) {
      console.error("Error liking character:", error);
    }
  };

  // Handle Pass
  const handlePass = () => {
    setFluttering("left");
    setTimeout(() => {
      setFluttering("");  // Reset flutter after animation
      fetchCharacter();   // Fetch next character
    }, 1500);  // Match the duration of the animation
  };

  // Load a character on mount
  useEffect(() => {
    fetchCharacter();
  }, []);

  return (
    <div className="swipes-page">
      {loading ? (
        <p>Loading character...</p>
      ) : character ? (
        <div
          className={`character-card ${fluttering ? `flutter-${fluttering}` : ""}`} // Apply the fluttering class
        >
          <img className="character-image" src={character.image_url} alt={character.name} />
          <h2>{character.name}</h2>
          <p>{character.description}</p>
          <div className="buttons">
            <button onClick={handlePass}>Pass</button>
            <button onClick={handleLike}>Like</button>
          </div>
        </div>
      ) : (
        <p>
          <div>You've reached the end! Add more characters you'd like!</div>
          <OpenModalButton
            buttonText="+ Create Character"
            modalComponent={<CharacterFormModal />}
          />
        </p>
      )}
    </div>
  );
}



















// export default function SwipesPage() {
//   const [character, setCharacter] = useState(null);
//   const [loading, setLoading] = useState(true);

//   // Fetch a random character
//   const fetchCharacter = async () => {
//     setLoading(true);
//     try {
//       const response = await fetch("/api/characters/random");
//       if (!response.ok) throw new Error("Failed to fetch character");
//       const data = await response.json();
//       setCharacter(data);
//     } catch (error) {
//       console.error("Error fetching character:", error);
//     } finally {
//       setLoading(false);
//     }
//   };

//   // Handle Like
//   const handleLike = async () => {
//     if (!character) return;
//     try {
//       const response = await fetch(`/api/characters/${character.id}/likes`, {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         credentials: "include", // Ensure cookies are sent
//       });

//       if (!response.ok) {
//         const data = await response.json();
//         console.error(data.error_message);

//         // If the user has liked all characters, show end message
//         if (response.status === 400) {
//           setCharacter(null); // This will trigger the "end" message
//         }
//         return;
//       }

//       // Successfully liked, fetch next character
//       fetchCharacter();
//     } catch (error) {
//       console.error("Error liking character:", error);
//     }
//   };


// //   const handleLike = async () => {
// //     if (!character) return;
// //     try {
// //       const response = await fetch(`/api/likes/${character.id}/likes`, {
// //         method: "POST",
// //         headers: { "Content-Type": "application/json" },
// //       });

// //       if (!response.ok) {
// //         const data = await response.json();
// //         console.error(data.error_message);
// //         return;
// //       }

// //       // Successfully liked, fetch next character
// //       fetchCharacter();
// //     } catch (error) {
// //       console.error("Error liking character:", error);
// //     }
// //   };

//   // Handle Pass
//   const handlePass = () => {
//     fetchCharacter(); // Just fetch a new character
//   };

//   // Load a character on mount
//   useEffect(() => {
//     fetchCharacter();
//   }, []);

//   return (
//     <div className="swipes-page">
//       {loading ? (
//         <p>Loading character...</p>
//       ) : character ? (
//         <div className="character-card">
//           <img className="character-image" src={character.image_url} alt={character.name} />
//           <h2>{character.name}</h2>
//           <p>{character.description}</p>
//           <div className="buttons">
//             <button onClick={handlePass}>Pass</button>
//             <button onClick={handleLike}>Like</button>
//           </div>
//         </div>
//       ) : (
//         <p>
//             <div>
//                 You've reached the end! Add more characters you'd like!
//             </div>
//             <div> <>
//               <OpenModalButton
//                  buttonText="+ Create Character"
//                  modalComponent={<CharacterFormModal />}
//               />

//             </></div>

//         </p>

//       )}
//     </div>
//   );
// }
