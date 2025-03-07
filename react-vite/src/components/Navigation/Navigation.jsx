import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <nav className="navbar">
      <div className="left">
        <NavLink to="/" className="nav-link">
          <img src="/public/blackFire.png" alt=""  className="logo"/>
        </NavLink>
      </div>
      <div className="right">
        <ProfileButton />
      </div>
    </nav>
  );
}

export default Navigation;





// import { NavLink } from "react-router-dom";
// import ProfileButton from "./ProfileButton";
// import "./Navigation.css";

// function Navigation() {
//   return (
//     <ul>

//       <NavLink to="/">Hear Me Out?</NavLink>

//       <ProfileButton />
//     </ul>
//   );
// }

// export default Navigation;
