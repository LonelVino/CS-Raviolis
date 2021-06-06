<template>
  <div>
    <el-menu-item @click="filterProd()">
      <item :title="item" />
    </el-menu-item>
  </div>
</template>

<script>
import Item from './Item'
import FixiOSBug from './FixiOSBug'
import {getAllProdsByCat } from '@/api/shop.js'
import { mapGetters } from 'vuex';


export default {
  name: 'SidebarItem',
  components: { Item },
  mixins: [FixiOSBug],
  props: {
    // route object
    id: {
      type: Number,
      required: true
    },
    item: {
      type: String,
      required: true
    },

  },
  computed: {
    ...mapGetters([
      'prods_loading'
    ])
  },
  data() {
    // To fix https://github.com/PanJiaChen/vue-admin-template/issues/237
    // TODO: refactor with render function
    return {}
  },
  mounted() {
    // console.log(this.item)
  },
  methods: {
    filterProd() {
      getAllProdsByCat(this.id).then(res => {
        this.$store.dispatch('product/changeProdsLoading', true)
        console.log('prods_loading'.toUpperCase(), +this.prods_loading)
        const prodsByCat = res.data.prod_infos
        this.$store.dispatch('product/setProductsByCat', prodsByCat)
        setTimeout(() => {
            this.$store.dispatch('product/changeProdsLoading', false)
        }, 1000);
        // console.log('prods_loading'.toUpperCase(), +this.prods_loading)

      }).catch(err => {
        console.error(err)
      })
    }
  }
}
</script>


<style lang="scss" scoped>
.title {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>