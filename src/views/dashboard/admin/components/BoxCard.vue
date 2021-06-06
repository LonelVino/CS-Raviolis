<template>
  <el-card class="box-card-component" style="margin-left:8px;">
    <div slot="header" class="box-card-header">
      <img src="https://wpimg.wallstcn.com/e7d23d71-cf19-4b90-a1cc-f56af8c0903d.png">
    </div>
    <div class="desc">
      <div class="progress-title">
        <span>{{item.name}}</span>
      </div>
      <div class="progress-item">
        <span>Price:{{item.price}}</span>
      </div>
      <div class="progress-item">
        <span>Minimum: {{item.quantity_unit}}</span>
      </div>
      <div class="progress-item">
        <span>Discount: {{item.dt_info}}</span>
      </div>
    </div>
    
  </el-card>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  components: { },
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  filters: {
    statusFilter(status) {
      const statusMap = {
        success: 'success',
        pending: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      statisticsData: {
        article_count: 1024,
        pageviews_count: 1024
      }
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  created() {
    console.log(this.item)
  }
}
</script>

<style lang="scss" >
.box-card-component{
  .el-card__header {
    padding: 0px!important;
  }
}
</style>
<style lang="scss" scoped>
.box-card-component {
  .box-card-header {
    position: relative;
    height: 220px;
    img {
      width: 100%;
      height: 100%;
      transition: all 0.2s linear;
      &:hover {
        transform: scale(1.1, 1.1);
        filter: contrast(130%);
      }
    }
  }
  .desc {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items:flex-start;
  }
  .progress-title {
    margin-bottom: 5px;
    font-size: 16px;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    font-weight: bolder;
  }
  .progress-item {
    margin-bottom: 5px;
    font-size: 13px;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-weight: bold;
  }
  @media only screen and (max-width: 100px){
    
  }
}
</style>
