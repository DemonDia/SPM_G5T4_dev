export default({
  namespaced: true,
  state: {
    user: null,
  },
  mutations: {
    //

    SET_USER(state, userData) {
      state.user = userData
      //localStorage.setItem('user', JSON.stringify(userData))
    }
    
  },
  actions: {
    async login({ dispatch }, credentials) {
      // fake login here without backend api
      // break credentials into email, role, name into a single user object

      let role = ''
      let name = ''

      if (credentials.email === '' || credentials.password === '') {
        throw new Error('Please provide valid credentials')
      } else if(credentials.email === 'admin@ljms.com' && credentials.password === '123456') {
        // admin
        role = 'admin'
        name = 'Alan Walker'
      } else if(credentials.email === 'manager@ljms.com' && credentials.password === '123456') { 
        //
        role = 'manager'
        name = 'David Guetta'
      } else if(credentials.email === 'staff@ljms.com' && credentials.password === '123456') {
        //
        role = 'staff'
        name = 'Martin Garrix'
      } else {
        //
        throw new Error('User not found')
      }

      let user = {name: name, role: role, email: credentials.email}

      dispatch('attempt', user)

    },

    async attempt({ commit, state }, user) {
      if (user) {
        commit('SET_USER', user)
      }

      if (!state.user) {
        return
      }
    }


  },
});