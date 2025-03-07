import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import OpenModalButton from "../OpenModalButton";
import "../LandingPage/LandingPage.css"


export default function LandingPage() {
  return (
    <div className="landing-container">
      <h1 className="title">Hear Me Out?</h1>
      <div className="button-group">
        <OpenModalButton
          buttonText="Log In"
          modalComponent={<LoginFormModal />}
        />
        <OpenModalButton
          buttonText="Create Account"
          modalComponent={<SignupFormModal />}
        />
      </div>
    </div>
  );
}




// import { useNavigate } from "react-router-dom";

// export default function LandingPage() {
//   const navigate = useNavigate();

//   return (
//     <div className="landing-container">
//       <h1 className="title">Hear Me Out?</h1>
//       <div className="button-group">
//         <button onClick={() => navigate("/login")}>Log In</button>
//         <button onClick={() => navigate("/signup")}>Create Account</button>
//       </div>
//     </div>
//   );
// }

// import { useState } from "react";
// import { useModal } from "../../context/Modal"; // Import the useModal hook

// export default function LandingPage() {
//   const { setModalContent, setOnModalClose } = useModal();

//   // Function to open the Login Modal
//   const openLoginModal = () => {
//     setModalContent(
//       <div>
//         <h2>Log In</h2>
//         <form onSubmit={handleLogin}>
//           <label>
//             Email:
//             <input type="email" required />
//           </label>
//           <label>
//             Password:
//             <input type="password" required />
//           </label>
//           <button type="submit">Log In</button>
//         </form>
//       </div>
//     );
//     setOnModalClose(() => closeLoginModal);
//   };

//   // Function to open the Create Account Modal
//   const openCreateAccountModal = () => {
//     setModalContent(
//       <div>
//         <h2>Create Account</h2>
//         <form onSubmit={handleCreateAccount}>
//           <label>
//             Username:
//             <input type="text" required />
//           </label>
//           <label>
//             Email:
//             <input type="email" required />
//           </label>
//           <label>
//             Password:
//             <input type="password" required />
//           </label>
//           <button type="submit">Create Account</button>
//         </form>
//       </div>
//     );
//     setOnModalClose(() => closeCreateAccountModal);
//   };

//   // Log in handler (You can add your own logic here)
//   const handleLogin = (e) => {
//     e.preventDefault();
//     // Add your login logic
//     console.log("Logged in!");
//   };

//   // Create account handler (Add your logic here)
//   const handleCreateAccount = (e) => {
//     e.preventDefault();
//     // Add your account creation logic
//     console.log("Account created!");
//   };

//   return (
//     <div className="landing-container">
//       <h1 className="title">Hear Me Out?</h1>
//       <div className="button-group">
//         <button onClick={openLoginModal}>Log In</button>
//         <button onClick={openCreateAccountModal}>Create Account</button>
//       </div>
//     </div>
//   );
// }
