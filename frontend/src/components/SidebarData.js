import React from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
import * as FcIcons from "react-icons/fc";
import * as GrIcons from "react-icons/gr"

export const SidebarData = [
  {
    title: "Home",
    path: "/",
    icon: <AiIcons.AiFillHome />,
    cName: "nav-text",
  },
  {
    title: "About",
    path: "/about",
    icon: <FaIcons.FaInfoCircle />,
    cName: "nav-text",
  },
  {
    title: "Contact",
    path: "/contact",
    icon: <AiIcons.AiFillContacts />,
    cName: "nav-text",
  },
  {
    title: "Protocols",
    path: "/protocol",
    icon: <IoIcons.IoIosBook />,
    cName: "nav-text",
  },
//   {
//     title: "Messages",
//     path: "/messages",
//     icon: <FaIcons.FaEnvelopeOpenText />,
//     cName: "nav-text",
//   },
//   {
//     title: "Support",
//     path: "/support",
//     icon: <IoIcons.IoMdHelpCircle />,
//     cName: "nav-text",
//   },
];