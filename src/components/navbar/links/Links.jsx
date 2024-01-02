// "use client";


// import React, { useState } from 'react'
// import styles from './links.module.css'
// import NavLink from './navLink/navLink';

// const link = [
//     {
//       title: "Homepage",
//       path: "/",
//     },
//     {
//       title: "About",
//       path: "/about",
//     },
//     {
//       title: "Contact",
//       path: "/contact",
//     },
//     {
//       title: "Blog",
//       path: "/blog",
//     },
//   ];

//   const Links = () => {
//     const [open,setOpen] = useState(false)
//   }
  
//   const session = true
//   const isAdmin  = true


// function Links() {
//   return (
//     <div className={styles.links}>
//         {link.map((link=>
//             // <Link href={link.path}>{link.title}</Link>
//             <NavLink item={link} key={link.title}/>
//             ))}{
//                session ? (
//                 <>
                
                
//                 {
//                   isAdmin && (
//                     <NavLink item={{ title: "Admin", path: "/admin" }} />
//                   )
//                 }
//                 <button className={styles.logout}>Logout</button>
//                 </>
//                ) : (
//                 <NavLink item={{ title: "Login", path: "/login" }} />
//                ) 
//             }
//     </div>
//   )
// }



// export default Links

"use client";

import React, { useState } from 'react';
import styles from './links.module.css';
import NavLink from './navLink/navLink';

const link = [
  {
    title: "Homepage",
    path: "/",
  },
  {
    title: "About",
    path: "/about",
  },
  {
    title: "Contact",
    path: "/contact",
  },
  {
    title: "Blog",
    path: "/blog",
  },
];

const Links = () => {
  const [open, setOpen] = useState(false);

  const session = true;
  const isAdmin = true;

  return (
    <div className={styles.container}>
      <div className={styles.links}>
        {link.map((link) => (
          <NavLink item={link} key={link.title} />
        ))}
        {session ? (
          <>
            {isAdmin && (
              <NavLink item={{ title: "Admin", path: "/admin" }} />
            )}
            <button className={styles.logout}>Logout</button>
          </>
        ) : (
          <NavLink item={{ title: "Login", path: "/login" }} />
        )}
      </div>

      {/* <button onClick={() => setOpen((prev) => !prev)}>Menu</button> */}
      {open && (
        <div className={styles.mobileLinks}>
          {link.map((link) => (  
            <NavLink item={link} key={link.title} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Links;
