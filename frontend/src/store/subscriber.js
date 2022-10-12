import store from '@/store'


store.subscribe((mutation, state) => {
    // Store the state object as a JSON string
    switch(mutation.type) {
        case 'auth/SET_USER':
            if(mutation.payload) {
                //localStorage.setItem('token', mutation.payload) --> returns object which causes error
            } else if(mutation.payload == 'undefined' || mutation.payload == null) {
                localStorage.removeItem('token')
            }
            break;
    }
})