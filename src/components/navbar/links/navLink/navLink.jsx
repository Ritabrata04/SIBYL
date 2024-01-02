"use client";

import Link from "next/link";
import styles from "./navLink.module.css";
import { usePathname } from "next/navigation";

const NavLink = ({ item }) => {
  const pathName = usePathname();

  return (
    <Link
      href={item.path}
      className={`${styles.container} ${
        pathName === item.path && styles.active
      }`}
    >
      {item.title}
    </Link>
  );
};

export default NavLink;

// import React from 'react'
// import styles from "./navLink.module.css"

// function NavLink({item}) {
//   return (
//     <div>
//         <Link href={link.path}>{link.title}</Link>
//     </div>
//   )
// }

// export default NavLink