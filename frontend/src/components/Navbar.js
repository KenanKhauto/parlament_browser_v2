import React, { useState } from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import { Link } from "react-router-dom";
import { SidebarData } from "./SidebarData";
import "../App.css";
import { IconContext } from "react-icons";
import * as IoIcons from "react-icons/io";

function Navbar() {
  const [sidebar, setSidebar] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");

  const showSidebar = () => setSidebar(!sidebar);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    // Handle database stuff here
    if (searchQuery !== ""){
        console.log("Search query:", searchQuery);
    }
    
  };

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  return (
    <>
      <IconContext.Provider value={{ color: "undefined" }}>
        <div className="navbar">
            <div>
                <Link to="#" className="menu-bars">
                    <FaIcons.FaBars onClick={showSidebar} />
                </Link>
            </div>
         
            <div className="navbar-right">
                <div className="search-form">
                    <button className="search-button" onClick={handleSearchSubmit}>
                        <IoIcons.IoMdSearch/>
                        </button>
                    <input
                        className="search-input"
                        type="text"
                        placeholder="Search..."
                        value={searchQuery}
                        onChange={handleSearchChange}
                    />
                </div>

                <div className="login-register">
                    <Link className="login-register-link" to="/login">
                    <IoIcons.IoIosLogIn />
                        <span>Login</span>
                    </Link>
                    <Link className="login-register-link" to="/register">
                    <AiIcons.AiOutlineLogin />
                    <span>Register</span>
                    </Link>
                </div>
            </div>
          </div>  
        
        <nav className={sidebar ? "nav-menu active" : "nav-menu"}>
          <ul className="nav-menu-items" onClick={showSidebar}>
            <li className="navbar-toggle">
              <Link to="#" className="menu-bars">
                <AiIcons.AiOutlineClose />
              </Link>
            </li>
            {SidebarData.map((item, index) => {
              return (
                <li key={index} className={item.cName}>
                  <Link to={item.path} >
                    {item.icon}
                    <span>{item.title}</span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
      </IconContext.Provider>
    </>
  );
}

export default Navbar;