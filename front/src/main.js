import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './plugins/vuetify'
// import Vuetify from 'vuetify'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
// Vue.use(Vuetify)
// axios.defaults.withCredentials = true;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
