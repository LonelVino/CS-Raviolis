<template>
  <div class="app-container">
    <div class="orders" v-for="order in orders">
      <div class="user-order">
        <el-row :gutter="12">
          <el-col :span="6">
            <el-card shadow="hover">
              Has gotten:  {{order.gotten}}
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              Total Price:  {{order.usr_price}}
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              Has paid:  {{order.paid}}
            </el-card>
          </el-col>

          <el-col :span="6">
            <el-card shadow="hover">
              Create Time:  {{order.created}}
            </el-card>
          </el-col>
        </el-row>
      </div>
      <el-table
        ref="multipleTable"
        :key="tableKey"
        v-loading="listLoading"
        :data="order.order_items"
        border
        fit
        highlight-current-row
        style="width: 100%;">
        <el-table-column prop="id" label="ID" width="50px" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Product" width="200px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.prod_name }}</div>
          </template>
        </el-table-column>
        <el-table-column prop="mini_num" label="Num(/1 Unit)" width="150px" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column prop="itm_price" label="Unit Price" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column prop="quantity" label="Quantity"  align="center" show-overflow-tooltip></el-table-column>
        <el-table-column prop="ttl_price" label="Total" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Has Gotten" width="100px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
          <el-switch
              v-model="scope.row.gotten"
              :active-value="1"
              :inactive-value="0"
              active-color="#02538C"
              inactive-color="#B9B9B9"
              @change="handleChangeGotten(scope.row)"
            />
          </template>
        </el-table-column>
        <el-table-column label="Actions" align="center" class-name="small-padding fixed-width">
          <template slot-scope="{row}">
            <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="confirmDelete(row.id)">
              Remove
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="remove-all">
      <el-button type="danger" @click="confirmDeleteAll()">Remove All</el-button>
    </div>
  </div>
</template>

<script>
import {getProd} from '@/api/shop.js'
import {getOneOrderItem, getUserOneOrder, getUserAllOrders, getOneOrderItems, checkUserOneItem,
 checkUserAllItems, deleteUserOrderItem, deleteUserOrder,  deleteUserAllOrders} from '@/api/order.js'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves' // waves directive

export default {
  name: 'OrderTable',
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      listLoading: false,
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

      usr_id: 13,    //TODO: tobe modified
      order_items: null,
      orders: null,
      all_order_items: [],

      tmp_prod_info: null,
      idx: 0,

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
    async getList() {
      this.listLoading = true
      var res = await getUserAllOrders(this.usr_id)
      this.orders = res.data.order_infos
      for(var i = 0; i < this.orders.length;i++) {
        getOneOrderItems(this.orders[i].id).then(response => {
          // console.log('Original Order Items:', response.data.order_items_info)
          this.all_order_items.push(response.data.order_items_info) 
          this.getProdbyId(this.idx).then(this.idx++)
          setTimeout(() => {
            this.listLoading = false
          }, 1500);
        }).catch(err => {
          console.error(err)
        })
      }
      console.log('ORDERS:', this.orders)
      console.log('ALL ORDER ITEMS:', this.all_order_items)
    },

    //TODO: modify the product request function
    async getProdbyId(idx) {
      // console.log('INDEX WHEN GETTING PRODUCT BY ORDER_ID:', idx)
      this.all_order_items[idx].prod_name = ''; this.all_order_items[idx].dt_info = ''; this.all_order_items[idx].mini_num = '';
      for(var j=0; j<this.all_order_items[idx].length; j++) {
        var prod_info = await getProd(this.all_order_items[idx][j].product_id)
        this.tmp_prod_info = prod_info.data.prod_info
        Object.assign(this.all_order_items[idx][j], {
          prod_name: this.tmp_prod_info.name,
          dt_info: this.tmp_prod_info.dt_info,
          mini_num: this.tmp_prod_info.quantity_unit,
        })
        this.all_order_items[idx][j].gotten = (this.all_order_items[idx][j].gotten==true || this.all_order_items[idx][j].gotten==1) ? 1 : 0
        this.$set(this.all_order_items[idx][j], 'ttl_price',  this.all_order_items[idx][j].itm_price * this.all_order_items[idx][j].quantity)
        this.orders[idx].usr_price += this.all_order_items[idx][j].itm_price * this.all_order_items[idx][j].quantity
      }
      // console.log(idx, this.orders[idx], this.all_order_items[idx])
      Object.assign(this.orders[idx], {
        order_items: this.all_order_items[idx]
      })
      this.orders[idx].created = this.orders[idx].created.substr(5,5)
    },

    handleChangeGotten(row){
      let payload = {'id': row.id, 'gotten': row.gotten}
      checkUserOneItem(payload).then(res => {
        const status = (row.gotten == 0) ? 'False' : 'True'
        this.$notify({
          title: 'Success',
          message: 'Status Changed into ' + status.toUpperCase(),
          type: 'success',
          duration: 2000
        })
      })
    },

    confirmDeleteOrder(index) {
      this.$confirm('This operation will delete this information forever, are you sure?', 'Note', {
        confirmButtonText: 'Confirm',
        cancelButtonText: 'Cancle',
        type: 'warning'
      }).then(() => {
        this.handleDeleteOrder(index)
      }).catch(() => {
        this.$message({
          type: 'info',
          message: 'Delete cancled'
        });
      });
    },

    handleDeleteOrder(index) {
      console.log('INDEX:', index)
      deleteUserOrder(index).then(() => {
        this.$notify({
          title: 'Success',
          message: 'Delete Successfully',
          type: 'success',
          duration: 2000
        })
        this.getList()
      }).catch(err => {
        this.$notify({
          title: 'Failed',
          message: 'Delete failed',
          type: 'danger',
          duration: 2000
        })
      })
    },

    confirmDeleteAllOrders() {
      this.$confirm('This operation will delete this information forever, are you sure?', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.handleDeleteAllOrders(this.usr_id)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Delete cancled'
          });
        });
    },
    handleDeleteAllOrders(index) {
      console.log('INDEX:', index)
      deleteUserAllOrders(index).then(() => {
        this.$notify({
          title: 'Success',
          message: 'Delete All Successfully',
          type: 'success',
          duration: 2000
        })
        this.getList()
      }).catch(err => {
        this.$notify({
          title: 'Failed',
          message: 'Delete All failed',
          type: 'danger',
          duration: 2000
        })
      })
    },
  }
}
</script>

<style lang="scss">
.number-count {
  transition: 0.7s ;
  width: 10vw !important;
}
@media screen and (max-width: 1000px) {
.number-count {
  width: 15vw !important;
}
}
</style>

<style scoped>
.user-order {
  margin: 20px 0px;
}
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
.remove-all {
  margin: 20px auto;
  display: flex;
  flex-direction: row;
  justify-content: start;
}
</style>