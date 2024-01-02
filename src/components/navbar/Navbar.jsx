import React from 'react'
import Link from 'next/link'
import Links from './links/Links'
import styles from "./navbar.module.css"

function Navbar() {
  return (
    <div className={styles.container}>
    <div className={styles.logo}>Logo</div>
    <div>
        {/* <Link href='/'>Home</Link>
        <Link href='/about'>About</Link>
        <Link href='/contact'>Contact</Link>
        <Link href='/blog'>Blog</Link>
        <Link href='/login'>Login</Link> */}
        <Links/>

    </div>
    </div>
       
  )
}

export default Navbar