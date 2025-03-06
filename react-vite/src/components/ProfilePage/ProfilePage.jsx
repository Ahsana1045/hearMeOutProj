import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import CharacterFormModal from "../CharacterFormModal/CharacterFormModal"; // Import CharacterForm modal
// import "./ProfilePage.css"; #ADD LATER

function ProfilePage() {
  const user = useSelector((state) => state.session.user);
  const { openModal } = useModal();
  const [userCharacters, setUserCharacters] = useState([]);
  const [topLikedCharacters, setTopLikedCharacters] = useState([]);

  useEffect(() => {
    if (user) {
      // Fetch characters created by the user
      fetch(`/api/characters`)
        .then((res) => res.json())
        .then((data) => {
          const userChars = data.filter((char) => char.user_id === user.id);
          setUserCharacters(userChars);
        });

      // Fetch top 5 most liked characters
      fetch(`/api/characters/top-liked`)
        .then((res) => res.json())
        .then(setTopLikedCharacters);
    }
  }, [user]);

  if (!user) return <h2>Please log in to view your profile.</h2>;

  return (
    <div className="profile-page">
      <h1>{user.username}'s Profile</h1>

      <OpenModalButton
        buttonText="+ Create Character"
        modalComponent={<CharacterFormModal />}
        />


      {/* <button onClick={() => openModal(<CharacterFormModal />)}>
        + Create Character
      </button> */}

      <h2>Your Characters</h2>
      <div className="character-list">
        {userCharacters.length ? (
          userCharacters.map((char) => (
            <div key={char.id} className="character-card">
              <img src={char.image_url} alt={char.name} />
              <h3>{char.name}</h3>
              <p>{char.description}</p>
            </div>
          ))
        ) : (
          <p>You haven't created any characters yet.</p>
        )}
      </div>

      <h2>Top 5 Most Liked Characters</h2>
      <div className="character-list">
        {topLikedCharacters.length ? (
          topLikedCharacters.map((char) => (
            <div key={char.id} className="character-card">
              <img src={char.image_url} alt={char.name} />
              <h3>{char.name}</h3>
              <p>{char.description}</p>
              <p>Likes: {char.like_count}</p>
            </div>
          ))
        ) : (
          <p>No liked characters yet.</p>
        )}
      </div>
    </div>
  );
}

export default ProfilePage;
