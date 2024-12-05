<template>
  <img alt="Vue logo" src="./assets/logo.png">
  
  <div id="app">
    <AgendaContactos />
  </div>

</template>

<script>
import AgendaContactos from './components/AgendaContactos.vue';

export default {
  name: 'App',
  components: {
    AgendaContactos
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
