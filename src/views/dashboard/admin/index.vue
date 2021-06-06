<template>
  <div class="dashboard-editor-container">
    <PanelGroup/>
    <el-main>
      <sequential-entrance>
        <el-row :gutter="8" v-loading="prods_loading">
          <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;" v-for="prod in productByCat">
            <template>
              <box-card :item=prod ></box-card>
            </template>
          </el-col>
        </el-row>
        </sequential-entrance>
    </el-main>
    
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import {getAllCats, getAllProds, getAllProdsByCat} from '@/api/shop.js'
import PanelGroup from './components/SideBar/PanelGroup'
import BoxCard from './components/BoxCard'


export default {
  name: 'DashboardAdmin',
  components: {
    PanelGroup,
    BoxCard,
  },
  data() {
    return {
      type: '',
    }
  },
  computed: {
    ...mapGetters([
      'products',
      'productByCat',
      'categories',
      'prods_loading'
    ]),
  },
  created() {
    this.getList()
    console.log(this.prods_loading)
  },
  methods: {
    getList() {
      this.listLoading = true
      getAllCats().then(response => {
        const cats = response.data.cat_infos
        this.$store.dispatch('product/setCategories', cats)
      }).catch(err => {
        console.error(err)
      })
      getAllProds().then(response => {
        const prods = response.data.prod_infos
        this.$store.dispatch('product/setProducts', prods)
      }).catch(err => {
        console.error(err)
      })
      getAllProdsByCat(1).then(response => {
        const prodsByCat = response.data.prod_infos
        this.$store.dispatch('product/setProductsByCat', prodsByCat)
      }).catch(err => {
        console.error(err)
      })
      this.listLoading = false
    },
    //TODO: Pagination
    handleSetProducts(type) {
      this.type = type
      // Get the products according to the type
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  position: relative;
  display: flex;
  flex-direction: row;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
