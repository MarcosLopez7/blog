import { createStore } from "vuex";

export default createStore({
  state: {
    loginVisible: false,
    signUpVisible: false,
    isUserCreated: false,
  },
  mutations: {
    SET_LOGIN_VISIBILITY(state, visibleValue) {
      state.loginVisible = visibleValue;
    },
    SET_SIGN_UP_VISIBILITY(state, visibleValue) {
      state.signUpVisible = visibleValue;
    },
    SET_IS_USER_CREATED(state, value) {
      state.isUserCreated = value;
    },
  },
  actions: {
    changeLoginVisibility({ commit, state }) {
      commit("SET_LOGIN_VISIBILITY", !state.loginVisible);
    },
    changeSignUpVisibility({ commit, state }) {
      commit("SET_SIGN_UP_VISIBILITY", !state.signUpVisible);
    },
    setIsUserCreated({ commit }, value) {
      commit("SET_IS_USER_CREATED", value);
    },
  },
  modules: {},
});
