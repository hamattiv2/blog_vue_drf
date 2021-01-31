<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <HelloWorld/>

      <h2>ここに結果が表示されます → {{ result }}</h2>
      <button @click="getAPI()">クリック！</button>

    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
      result: 'No Result',
      url: 'http://localhost:8000/blog/get/'
    }
  },
  methods: {
    getAPI () {
      this.$axios.get(this.url)
      .then(response => {
        this.result = response.data.data.status
      })
      .catch(() => {
        console.log('aaaa')
      })
    }
  }

}
</script>
