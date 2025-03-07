import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
// import "./CharacterForm.css"; # ADD LATERRR

  function CharacterFormModal({ character = null }) {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const [name, setName] = useState(character ? character.name : "");
  const [description, setDescription] = useState(character ? character.description : "");
  const [imageUrl, setImageUrl] = useState(character ? character.image_url : "");
  const [errors, setErrors] = useState({});
  const isEditing = !!character;


  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    if (name.length < 1 || description.length < 1 || imageUrl.length < 1) {
      return setErrors({ message: "All fields are required." });
    }

    const characterData = { name, description, image_url: imageUrl };
    const method = isEditing ? "PUT" : "POST";
    const url = isEditing ? `/api/characters/${character.id}` : "/api/characters";

    try {
      const response = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(characterData),
      });

      const data = await response.json(); // Always parse the response first

      if (response.ok) {
        closeModal();
        window.location.reload(); // Refresh to show updated character
      } else {
        setErrors({ message: data.error || "Failed to save character." });
      }
    } catch (err) {
      console.error("Error saving character:", err);
      setErrors({ message: "Something went wrong. Please try again later." });
    }
  };


  // const handleSubmit = async (e) => {
  //   e.preventDefault();
  //   setErrors({});

  //   if (name.length < 1 || description.length < 1 || imageUrl.length < 1) {
  //     return setErrors({ message: "All fields are required." });
  //   }

  //   const newCharacter = {
  //     name,
  //     description,
  //     image_url: imageUrl,
  //   };

  //   try {
  //     const response = await fetch(`/api/characters`, {
  //       method: "POST",
  //       headers: { "Content-Type": "application/json" },
  //       body: JSON.stringify(newCharacter),
  //     });

  //     if (response.ok) {
  //       closeModal();
  //       window.location.reload(); // Refresh to show new character
  //     } else {
  //       const data = await response.json();
  //       setErrors(data.errors || { message: "Failed to create character." });
  //     }
  //   } catch (err) {
  //     console.error("Error creating character:", err);
  //   }
  // };
  return (
    <div className="character-form-modal">
      <h1>{isEditing ? "Update Character" : "Create a Character"}</h1>
      {errors.message && <p className="error">{errors.message}</p>}
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <label>
          Description:
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            maxLength="100"
            required
          />
        </label>
        <label>
          Image URL:
          <input
            type="text"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            required
          />
        </label>
        <button type="submit">{isEditing ? "Update" : "Create"}</button>
      </form>
    </div>
  );

  // return (
  //   <div className="character-form-modal">
  //     <h1>Create a Character</h1>
  //     {errors.message && <p className="error">{errors.message}</p>}
  //     <form onSubmit={handleSubmit}>
  //       <label>
  //         Name:
  //         <input
  //           type="text"
  //           value={name}
  //           onChange={(e) => setName(e.target.value)}
  //           required
  //         />
  //       </label>
  //       <label>
  //         Description:
  //         <input
  //           type="text"
  //           value={description}
  //           onChange={(e) => setDescription(e.target.value)}
  //           maxLength="100"
  //           required
  //         />
  //       </label>
  //       <label>
  //         Image URL:
  //         <input
  //           type="text"
  //           value={imageUrl}
  //           onChange={(e) => setImageUrl(e.target.value)}
  //           required
  //         />
  //       </label>
  //       <button type="submit">Create</button>
  //     </form>
  //   </div>
  // );
}

export default CharacterFormModal;
