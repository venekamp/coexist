import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiBaseURL: 'http://localhost:8000',
    hasAuthenticatedUser: false
  },
  mutations: {
    change(state, hasAuthenticatedUser) {
      state.hasAuthenticatedUser = hasAuthenticatedUser;
    }
  },
  actions: {}
});
