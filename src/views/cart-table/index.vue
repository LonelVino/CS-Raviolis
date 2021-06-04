<template>
  <div class="app-container">
    <el-table
      ref="multipleTable"
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange"
      v-fit-columns
    >
      <el-table-column prop="id" label="ID" sortable="custom" align="center"></el-table-column>
      <el-table-column label="Product" width="200px" align="center">
        <template slot-scope="scope">
          <div> {{ scope.row.prod_name }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="prod_cat" label="Category" align="center"></el-table-column>
      <el-table-column label="Quantity" width="150px" align="center">
        <template slot-scope="scope">
          <div> {{ scope.row.quantity }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="unit_price" label="Unit Price" align="center"></el-table-column>
      <el-table-column prop="ttl_price" label="Total" align="center"></el-table-column>
      <el-table-column label="Actions" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="confirmDelete(row.id)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves' // waves directive

export default {
  name: 'cartTable',
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      list: null, 
      listLoading: true,
      tableKey: 0,
      showReviewer: false,

      temp: {
        id: undefined,
        quantity: 0,
        Product: {
          name: '',
          price: 0,
          min_num: 0,
          discout: '',
          cat: '',
        },
        total: 0,
      },

      // Edit dialog configuration
      dialogFormVisible: false,
      dialogStatus: '',
      confirmLoading: false,
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      // Get the cart data here
      this.listLoading = false
    },
    //TODO: Pagination

    compare(p) {
      return function(m,n){
        var a = m[p];
        var b = n[p];
        return b - a; //升序
      }
    },
    sortChange(data) {
      const { prop, order } = data
      this.tmp_list = this.list
      this.list.sort(this.compare("a_score"));
      console.log(this.list)
    },

    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      // Add the quantity here
    },

    confirmDelete(index) {
      this.$confirm('This operation will delete this information forever, are you sure?', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.handleDelete(index)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Delete cancled'
          });
        });
    },
    handleDelete(index) {
      console.log('INDEX:', index)
      // deleteInfo(index).then(() => {
      //   this.$notify({
      //     title: 'Success',
      //     message: 'Delete Successfully',
      //     type: 'success',
      //     duration: 2000
      //   })
      //   this.getList()
      // }).catch(err => {
      //   this.$notify({
      //     title: 'Failed',
      //     message: 'Delete failed',
      //     type: 'danger',
      //     duration: 2000
      //   })
      // })
    },
  }
}
</script>


<style scoped>
.note {
  display: flex;
  flex-direction: column;
  justify-content: start;
}
.note-txt {
  font-weight: bold;
  color:rgb(226, 134, 13);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 14px;
  margin: 0.2vw;
  display: flex;
  justify-content: flex-start;
}
</style>