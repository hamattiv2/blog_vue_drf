import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import Cookies from 'js-cookie';

Vue.config.productionTip = false
Vue.prototype.$axios = axios

// axios.defaults.baseURL = 'http://localhost:8000' //バックエンド側のIPとポート
// axios.defaults.headers.common['Accept'] = 'application/json'
// axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:8080'
// axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

axios.defaults.withCredentials = true;

export const GetDefaultHeader = () => {
  const csrfToken = Cookies.get('csrftoken');
  return {
      headers: {
          'X-CSRFToken': csrfToken
      }
  };
};

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
