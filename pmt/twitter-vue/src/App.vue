<template>
  <div id="app">
    <img src="./assets/logo.png">
    <Twitts/>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
// import TwittsList from './components/TwittsList'
import Twitts from './components/Twitts'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Twitts,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
