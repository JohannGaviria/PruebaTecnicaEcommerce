<template>
    <nav>
        <router-link to="/">Products</router-link> |
        <router-link to="/login">Login</router-link> |
        <router-link to="/register">Register</router-link>
    </nav>
    <router-view/>
</template>
  
<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f0f4f8;
    }

    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #4a90e2;
        color: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    header h1 {
        margin: 0;
        font-size: 1.8rem;
    }

    main {
        padding: 2rem 4rem;
    }

    nav {
        padding: 30px;
    }

    nav a {
        font-weight: bold;
        color: #2c3e50;
    }

    nav a.router-link-exact-active {
        color: #4a90e2;
    }
</style>
  