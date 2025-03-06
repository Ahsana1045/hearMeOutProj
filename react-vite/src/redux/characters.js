export const createCharacterThunk = (characterData) => async (dispatch) => {
    const response = await fetch("/api/characters", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(characterData),
    });

    if (response.ok) {
      const newCharacter = await response.json();
      dispatch(addCharacter(newCharacter)); // Assuming you have an action for adding
      return newCharacter;
    } else {
      const errorData = await response.json();
      return { errors: errorData };
    }
  };
