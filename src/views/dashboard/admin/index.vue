<template>
  <div class="dashboard-editor-container">
    <panel-group @handleSetProducts="handleSetProducts" />

    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
    </el-row>

    <el-row :gutter="8">
      <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;">
        <box-card />
      </el-col>
      <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;">
        <box-card />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import {getCat, getAllCats, getProd, getAllProds} from '@/api/shop.js'
import PanelGroup from './components/PanelGroup'
import BoxCard from './components/BoxCard'


export default {
  name: 'DashboardAdmin',
  components: {
    PanelGroup,
    BoxCard
  },
  data() {
    return {
      type: '',
      categories: [],
      products: []
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getAllCats().then(response => {
        this.categories = response.data.infos
        console.log('All categories: ', this.categories)
      }).catch(err => {
        console.error(err)
      })
      getAllProds().then(response => {
        this.products = response.data.infos
        console.log('All products: ', this.products)
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
  background-color: rgb(240, 242, 245);
  position: relative;

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
