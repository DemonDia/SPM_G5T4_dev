<template>
  <DashboardLayout>
    <h1>ROLES</h1>

    <div v-for="(value,key) in roles">
        <card-component :title=value.title :desc=value.desc />
    </div>
  </DashboardLayout>

</template>

<script>
import DashboardLayout from './Dashboard/Layout/DashboardLayout.vue';
import CardComponent from '../components/CardComponent.vue';
import axios from 'axios';

export default {
  name: "RoleView",
  components: {
    DashboardLayout,
    CardComponent
},
  mounted() {
   document.title = "LJMS - Roles";
  },
  data() {
    return {
      roles: [
        {
          title:"Sous Chef - Egg Machine",
          desc:"Beat 30 eggs in 1 second"
        }, 
        {
          title:"Role 2",
          desc:"gegg"
        }
      ]
    }
  },
  setup() {
    axios.get('http://localhost:3000/roles').then(response => {
      console.log(response.data);
    });
  }
};
</script>