export default({
  namespaced: true,
  state: {
    token: null,
    user: null,
  },
  mutations: {
    SET_USER(state, userData) {
      state.user = userData
      // localStorage.setItem('user', JSON.stringify(userData))
    },
    SET_TOKEN(state, token) {
      state.token = token
      localStorage.setItem('token', state.token)
    }
  },
  getters: {
    authenticated(state) {
      return state.user !== null
    }, 
    user(state) {
      return state.user
    }
  },
  actions: {
    async login({ dispatch }, credentials) {
      // fake login here without backend api
      // break credentials into email, role, name into a single user object
      let token = {admin: '000010000', user: '000020000', manager: '000030000', trainer: '000040000'};
      let staff = {
        admin: {staffID: '130001', email: 'jack.sim@allinone.com.sg', password: '123456'},
        user: {staffID: '140003', email: 'Janice.Chan@allinone.com.sg', password: '123456'},
        manager: {staffID: '140001', email: 'Derek.Tan@allinone.com.sg', password: '123456'},
        trainer: {staffID: '150175', email: 'Aiden.Tan@allinone.com.sg', password: '123456'},
      }


      if ((staff['admin'].staffID == credentials.staffID || staff['admin'].email == credentials.staffID)&& staff['admin'].password == credentials.password) {
        return dispatch('attempt', token.admin)
      } else if ((staff['user'].staffID == credentials.staffID || staff['user'].email == credentials.staffID)&& staff['user'].password == credentials.password) {
        return dispatch('attempt', token.user)
      } else if ((staff['manager'].staffID == credentials.staffID || staff['manager'].email == credentials.staffID)&& staff['manager'].password == credentials.password) {
        return dispatch('attempt', token.manager)
      } else if ((staff['trainer'].staffID == credentials.staffID || staff['trainer'].email == credentials.staffID)&& staff['trainer'].password == credentials.password) {
        return dispatch('attempt', token.trainer)
      } else {
        throw new Error('Invalid credentials')
      }

    },

    async attempt({ commit, state }, token) {

      
      // Admin -> 1
      // User -> 2
      // Manager -> 3
      // Trainer -> 4

      if (token) {
        commit('SET_TOKEN', token)
        if (token === '000010000') {
          commit('SET_USER', {StaffID: '130001',Staff_FName: 'John',Staff_LName: 'Sim', Dept: 'Chairman', Role: 1, Email: 'jack.sim@allinone.com.sg'})
        } else if (token === '000020000') {
          commit('SET_USER', {StaffID: '140003',Staff_FName: 'Janice',Staff_LName: 'Chan', Dept: 'Sales', Role: 2, Email: 'Janice.Chan@allinone.com.sg'})
        } else if (token === '000030000') {
          commit('SET_USER', {StaffID: '140001',Staff_FName: 'Derek',Staff_LName: 'Tan', Dept: 'Sales', Role: 3, Email: 'Derek.Tan@allinone.com.sg'})
        } else if (token === '000040000') {
          commit('SET_USER', {StaffID: '150175',Staff_FName: 'Aiden',Staff_LName: 'Tan', Dept: 'Ops', Role: 4, Email: 'Aiden.Tan@allinone.com.sg'})
        } else {
          commit('SET_USER', null)
        }
        
      }

      if (!state.user) {
        return
      }
    },


    signout({ commit }) {
      return new Promise((resolve) => {
        commit('SET_TOKEN', null)
        commit('SET_USER', null)
        localStorage.removeItem('token')
        resolve()
      })
    }


  },
});