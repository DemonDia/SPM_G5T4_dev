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
      // localStorage.setItem('token', token)
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
      
      let user = {name: '', role: '', email: ''};

      if (credentials.email === '' || credentials.password === '') {
        throw new Error('Please provide valid credentials')
      } else if(credentials.email === 'admin@ljms.com' && credentials.password === '123456') {
        // admin
        user = {name: 'Alan Walker', role: 'Admin', email: credentials.email, token: '000010000'}
      } else if(credentials.email === 'manager@ljms.com' && credentials.password === '123456') { 
        //
        user = {name: 'David Guetta', role: 'Manager', email: credentials.email, token: '000020000'}
      } else if(credentials.email === 'staff@ljms.com' && credentials.password === '123456') {
        //
        user = {name: 'Martin Garrix', role: 'Staff', email: credentials.email, token: '000030000'}
      } else {
        //
        throw new Error('User not found')
      }

    
      return dispatch('attempt', user)

    },

    async attempt({ commit, state }, user) {
      if (user) {
        commit('SET_USER', user)
        commit('SET_TOKEN', user.token)
      }

      if (!state.user) {
        return
      }
    }


  },
});