<template>
  <div class="main">
      <div class="container">

          <div class="col-md-12">

              <!-- Title Text -->
              <img src="https://i.imgur.com/i4JR9Ku.png">
              <h1 class="title-text col-md-12"> Binges Khan </h1>

              <Search />
              <!-- TODO Add Subtitle -->
              <!--<h3 class="subtitle-text col-md-12">Looking for a film to watch with your SO?-->
              <!--How about you expand the horizons of your mind with Khan Academy?</h3>-->

          </div>

      </div>

  </div>
</template>

<script>

import Vue from 'vue'
import Search from './Search'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import BarLoader from '@saeris/vue-spinners'

Vue.use(VueMaterial);

export default {
  name: 'HomePage',
  components: {
      Search,
      BarLoader
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
