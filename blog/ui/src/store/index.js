import { createStore } from "vuex";

export default createStore({
  state: {
    loginVisible: false,
  },
  mutations: {
    SET_LOGIN_VISIBILITY(state, visibleValue) {
      state.loginVisible = visibleValue;
    },
  },
  actions: {
    changeVisibility({ commit, state }) {
      commit("SET_LOGIN_VISIBILITY", !state.loginVisible);
    },
  },
  modules: {},
});
