import { createStore } from "vuex";

export default createStore({
  state: {
    loginVisible: false,
    signUpVisible: false,
  },
  mutations: {
    SET_LOGIN_VISIBILITY(state, visibleValue) {
      state.loginVisible = visibleValue;
    },
    SET_SIGN_UP_VISIBILITY(state, visibleValue) {
      state.signUpVisible = visibleValue;
    },
  },
  actions: {
    changeLoginVisibility({ commit, state }) {
      commit("SET_LOGIN_VISIBILITY", !state.loginVisible);
    },
    changeSignUpVisibility({ commit, state }) {
      commit("SET_SIGN_UP_VISIBILITY", !state.signUpVisible);
    },
  },
  modules: {},
});
