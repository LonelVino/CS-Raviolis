<template>
  <div class="prod_sidebar">
      <el-menu
        :default-active="activeMenu"
        :unique-opened="false"
        :collapse-transition="false"
        mode="vertical"
      >
        <sidebar-item v-for="cat in categories" :key="cat.id" :id="cat.id"  :item="cat.name"/>
      </el-menu>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import SidebarItem from './SidebarItem'
import variables from '@/styles/variables.scss'

export default {
  components: { SidebarItem },
  computed: {
    ...mapGetters([
      'sidebar',
      'categories'
    ]),
    activeMenu() {
      console.log('Activation!')
    },
    variables() {
      return variables
    },
    routes() {
      return this.$router.options.routes;
    }
  }
}
</script>

<style lang="scss">
.el-menu {
  color:chocolate !important;
  background: #EFEFBB;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to left, #D4D3DD, #EFEFBB);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to left, #D4D3DD, #EFEFBB); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}
.prod_sidebar {
  font-size: 20px !important;
  font-weight: bolder;
  background: #EFEFBB;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to left, #D4D3DD, #EFEFBB);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to left, #D4D3DD, #EFEFBB); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}
</style>