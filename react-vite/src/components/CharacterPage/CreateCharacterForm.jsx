import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { createCharacterThunk } from "../../redux/characters"; // You'll need to define this thunk
import "./CharacterForm.css";

function CharacterForm() {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    if (description.length > 100) {
      return setErrors({ description: "Description must be 100 characters or less." });
    }

    const newCharacter = { name, description, image_url: imageUrl };

    const response = await dispatch(createCharacterThunk(newCharacter));

    if (response.errors) {
      setErrors(response.errors);
    } else {
      closeModal();
    }
  };

  return (
    <div className="character-form">
      <h2>Create a Character</h2>
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
        {errors.name && <p className="error">{errors.name}</p>}

        <label>
          Description:
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </label>
        {errors.description && <p className="error">{errors.description}</p>}

        <label>
          Image URL:
          <input
            type="text"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            required
          />
        </label>
        {errors.image_url && <p className="error">{errors.image_url}</p>}

        <button type="submit">Create Character</button>
      </form>
    </div>
  );
}

export default CharacterForm;
