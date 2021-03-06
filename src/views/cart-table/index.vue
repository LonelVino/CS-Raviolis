<template>
  <div class="app-container">
    <div class="cart-table">
       <el-table
        ref="multipleTable"
        :key="tableKey"
        v-loading="listLoading"
        :data="cart_items"
        border
        fit
        highlight-current-row
        class="table"
        @sort-change="sortChange"
      >
        <el-table-column prop="id" label="ID" width="50px" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Product" width="200px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.prod_name }}</div>
          </template>
        </el-table-column>
        <el-table-column prop="mini_num" label="Num(1 Unit)" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Unit" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.itm_price }} €</div>
          </template>
        </el-table-column>
        <el-table-column label="Total" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.ttl_price }} €</div>
          </template>
        </el-table-column>
        <el-table-column prop="dt_info" label="Discount" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Quantity" width="250px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <el-input-number class='number-count' v-model="scope.row.quantity" @change="handleChangeQuantity(scope.row.id, scope.row.quantity)" :min="1" :step="1" ></el-input-number>
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
import {getCartByUser, getCartItems, addCart, updateCartItem, deleteCart, deleteCartItem} from '@/api/cart.js'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves' // waves directive

export default {
  name: 'cartTable',
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      list: null, 
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

      usr_id: 1,    // tobe modified
      cart: undefined,
      cart_items: null,

      tmp_prod_info: null,

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
      var res = await getCartByUser(this.usr_id)
      this.cart = res.data.cart_info
      //TODO:use aysnc/await to replace the settimeout
      getCartItems(this.cart.id).then(response => {
        this.cart_items = response.data.cart_itms_infos
        setTimeout(() => {
          this.getProdbyId()
          this.listLoading = false
        }, 1500);

      }).catch(err => {
        console.error(err)
      })
    },

    //TODO: Pagination
    async getProdbyId() {
      for(var i=0; i<this.cart_items.length; i++) {
        this.cart_items[i].prod_name = ''; this.cart_items[i].dt_info = ''; this.cart_items[i].mini_num = '';
        var prod_info = await getProd(this.cart_items[i].product_id)
        this.tmp_prod_info = prod_info.data.prod_info
        Object.assign(this.cart_items[i], {
          prod_name: this.tmp_prod_info.name,
          dt_info: this.tmp_prod_info.dt_info,
          mini_num: this.tmp_prod_info.quantity_unit,
        })
        this.$set(this.cart_items[i], 'ttl_price',  this.cart_items[i].itm_price * this.cart_items[i].quantity)
      }
      console.log('this.cart_items: ', this.cart_items)
    },


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

    handleChangeQuantity(id, quantity) {
      const payload = {'id': id,'quantity': quantity}
      updateCartItem(payload).then(res => {
        console.log(res)
      }).catch(err => {
        console.error(err)
      })
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
      deleteCartItem(index).then(() => {
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

    confirmDeleteAll() {
      this.$confirm('This operation will delete this information forever, are you sure?', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.handleDeleteAll(this.cart.id)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Delete cancled'
          });
        });
    },
    handleDeleteAll(index) {
      console.log('INDEX:', index)
      deleteCart(index).then(() => {
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

<style lang="scss" scoped>
.cart-table {
  background: linear-gradient(#a04949, #4b57dd);
  padding: 0.5vw 0.5vw;
  margin-bottom: 1vw;
  border-radius: 2%;
  display: flex;
  align-items: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.remove-all {
  margin: 20px auto;
  display: flex;
  flex-direction: row;
  justify-content: start;
}
</style>