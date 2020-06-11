// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import axios from 'axios'
// import VueAxios from 'vue-axios'
import router from './router'


// Vue.prototype.$http = axios
// Vue.use(VueAxios, axios)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#blog',  // html中的选择器
  router,
  components: { App },
  template: '<App/>'
})
