<template>
    <div>
    <!-- Menu for HR -->
    <TopMenu>
      <!-- <mobile-menu slot="content"></mobile-menu> -->
        <topmenu-link to="/admin/overview">
            <p>Home</p>
        </topmenu-link>
    </TopMenu>

    <!-- Main Content -->

    <slot />   

  </div>
</template>
<script>
    import TopMenu from '@/components/MenuPlugin/TopMenu.vue';

    export default {
      components: {
        TopMenu
      },
      data() {
        
      },
      methods: {
        
      }
    }
  </script>