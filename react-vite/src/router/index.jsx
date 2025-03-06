import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import ProfilePage from '../components/ProfilePage/ProfilePage';
import { useSelector } from 'react-redux';
import SwipesPage from '../components/SwipesPage/SwipesPage';
import LandingPage from '../components/LandingPage/LandingPage';


function RootPage() {
  const user = useSelector((state)=> state.session.user);

  return user ? <SwipesPage /> : <LandingPage />
}

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <RootPage />,
      },
      // {
      //   path: "/",
      //   element: <LandingPage />,
      // },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "profile",
        element: <ProfilePage />,
      },

    ],
  },
]);
