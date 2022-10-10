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

      if (credentials.email === '' || credentials.password === '') {
        throw new Error('Please provide valid credentials')
      } else if(credentials.email === 'admin@ljms.com' && credentials.password === '123456') {
        // admin
        return dispatch('attempt', token.admin)
      } else if(credentials.email === 'user@ljms.com' && credentials.password === '123456') { 
        // user
        return dispatch('attempt', token.user)
      } else if(credentials.email === 'manager@ljms.com' && credentials.password === '123456') {
        // manager
        return dispatch('attempt', token.manager)
      } else if(credentials.email === 'trainer@ljms.com' && credentials.password === '123456') {
        // trainer
        return dispatch('attempt', token.trainer)
      } else {
        // errors
        throw new Error('User not found')
      }
    

    },

    async attempt({ commit, state }, token) {

      // console.log(token)
      // Admin -> 1
      // User -> 2
      // Manager -> 3
      // Trainer -> 4

      if (token) {
        commit('SET_TOKEN', token)
        if (token === '000010000') {
          commit('SET_USER', {name: 'Alan Walker', role: 1, email: 'admin@ljms.com'})
        } else if (token === '000020000') {
          commit('SET_USER', {name: 'David Guetta', role: 2, email: 'user@ljms.com'})
        } else if (token === '000030000') {
          commit('SET_USER', {name: 'Martin Garrix', role: 3, email: 'manager@ljms.com'})
        } else if (token === '000040000') {
          commit('SET_USER', {name: 'Hardwell', role: 4, email: 'trainer@ljms.com'})
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