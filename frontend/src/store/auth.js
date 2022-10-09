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
      let token = {admin: '000010000', manager: '000020000', staff: '000030000'};

      if (credentials.email === '' || credentials.password === '') {
        throw new Error('Please provide valid credentials')
      } else if(credentials.email === 'admin@ljms.com' && credentials.password === '123456') {
        // admin
        return dispatch('attempt', token.admin)
      } else if(credentials.email === 'manager@ljms.com' && credentials.password === '123456') { 
        // manager
        return dispatch('attempt', token.manager)
      } else if(credentials.email === 'staff@ljms.com' && credentials.password === '123456') {
        // staff
        return dispatch('attempt', token.staff)
      } else {
        // errors
        throw new Error('User not found')
      }
    

    },

    async attempt({ commit, state }, token) {

      // console.log(token)

      if (token) {
        commit('SET_TOKEN', token)
        if (token === '000010000') {
          commit('SET_USER', {name: 'Alan Walker', role: 'Admin', email: 'admin@ljms.com'})
        } else if (token === '000020000') {
          commit('SET_USER', {name: 'David Guetta', role: 'Manager', email: 'manager@ljms.com'})
        } else if (token === '000030000') {
          commit('SET_USER', {name: 'Martin Garrix', role: 'Staff', email: 'staff@ljms.com'})
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