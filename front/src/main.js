import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
// import './plugins/vuetify'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
// Vue.prototype.$axios = (url, opts) => fetch(url, opts)
Vue.prototype.$postUrl = 'http://127.0.0.1:8000/blog/api/posts/'
Vue.prototype.$categoryUrl = 'http://127.0.0.1:8000/blog/api/categories/'
axios.defaults.withCredentials = true;


// axios.defaults.baseURL = 'http://localhost:8000' //バックエンド側のIPとポート
// axios.defaults.headers.common['Accept'] = 'application/json'
// axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:8080'
// axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
