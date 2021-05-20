<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-refresh-right" @click="ResetFilter">
        Reset
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        Export
      </el-button>
      <el-checkbox v-model="showReviewer" class="filter-item" style="margin-left:15px;" @change="tableKey=tableKey+1">
        reviewer
      </el-checkbox>
    </div>

    <div class="note">
      <p class="note-txt">When modifying the value of 'isAne', 'isVol', 'isPitch', 0 infers to 'No', 1 infers to 'Yes'!</p>
      <p class="note-txt">You can only modify one row at a time, not multiple rows of data.</p>
    </div>

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
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" width="100px" align="center">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.name }}</div>
          <div v-else>
            <el-input v-model="scope.row.name" @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="isAne" width="100px" align="center">
        <template slot-scope="scope">
          <span>{{scope.row.isAne?'Yes':'No'}}</span>
          <!-- <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.isAne?'Yes':'No' }}</div>
          <div v-else>
            <el-input v-model="scope.row.isAne" type='number' @click="handleClick(scope.row)"></el-input>
          </div> -->
        </template>
      </el-table-column>
      <el-table-column label="isVol" width="100px" align="center">
        <template slot-scope="scope">
          <span>{{scope.row.isVol?'Yes':'No'}}</span> 
          <!-- <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.isVol?'Yes':'No' }}</div>
          <div v-else>
            <el-input v-model="scope.row.isVol" type='number' @click="handleClick(scope.row)"></el-input>
          </div> -->
        </template>
      </el-table-column>
      <el-table-column label="isPitch" class-name="status-col" width="100px">
        <template slot-scope="scope">
          <span>{{scope.row.isPitch?'Yes':'No'}}</span>
          <!-- <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.isPitch?'Yes':'No' }}</div>
          <div v-else>
            <el-input v-model="scope.row.isPitch" type='number' @click="handleClick(scope.row)"></el-input>
          </div> -->
        </template>
      </el-table-column>

      <el-table-column label="Score" width="80px" sortable="custom"  align="center">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.score}}</div>
          <div v-else>
            <el-input v-model="scope.row.score" type='number' @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="Country" width="100px" sortable="custom" align="center">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.pays}}</div>
          <div v-else>
            <el-input v-model="scope.row.pays" @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="Email" class-name="status-col" width="200">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.email}}</div>
          <div v-else>
            <el-input v-model="scope.row.email" @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="Actions" align="center" width="350" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleSubmit(row)">
            Submit
          </el-button>
          <el-button type="warning" size="mini" @click="handleCancle(row)">
            Cancle
          </el-button>
          <el-button type="info" size="mini" @click="handleUpdate(row)">
            Edit in Dialog
          </el-button>
          <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="confirmDelete(row.id)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name">
          <el-input v-model="temp.name" />
        </el-form-item>
        <el-form-item label="Has played AneRouge?" prop="isAne" label-width="230px">
          <el-radio v-model="temp.isAne" label="1" disabled>Yes</el-radio>
          <el-radio v-model="temp.isAne" label="0" disabled>No</el-radio>
        </el-form-item>
        <el-form-item label="Has played Volant?" prop="isVol" label-width="230px">
          <el-radio v-model="temp.isVol" label="1" disabled>Yes</el-radio>
          <el-radio v-model="temp.isVol" label="0" disabled>No</el-radio>
        </el-form-item>
        <el-form-item label="Has played Pitch?" prop="isPitch" label-width="230px">
          <el-radio v-model="temp.isPitch" label="1" disabled>Yes</el-radio>
          <el-radio v-model="temp.isPitch" label="0" disabled>No</el-radio>
        </el-form-item>
        <el-form-item label="Score" prop="score" label-width="130px">
          <el-input v-model="temp.score" />
        </el-form-item>
        <el-form-item label="Country" prop="pays" label-width="130px">
          <el-input v-model="temp.pays" />
        </el-form-item>
        <el-form-item label="Email" prop="email" label-width="100px">
          <el-input v-model="temp.email" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" v-loading="confirmLoading" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {getAllInfos, addInfo, updateInfo, deleteInfo} from '@/api/user'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

export default {
  name: 'UserTable',
  components: { Pagination },
  directives: { waves },

  filters: {
    statusFilter(status) {
      const statusMap = {
        deleted: 'danger'
      }
      return statusMap[status]
    },
    typeFilter(type) {
      return calendarTypeKeyValue[type]
    }
  },

  data() {
    return {
      tableKey: 0,
      list: null,
      tmp_list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        name: undefined,
      },
      showReviewer: false,

      temp: {
        id: undefined,
        name: 'None',
        isAne: 0,
        isVol: 0,
        isPitch: 0,
        score: 0,
        email: '',
        telephone: 'None',
        loc: 'None',
        pays: 'None'
      },


      // Edit dialog configuration
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },

      rules: {
        name: [{ required: true, message: 'name is required', trigger: 'blur' }],
        isAne: [{ required: true, message: 'If has played AneRouge is required', trigger: 'change' }],
        isVol: [{ required: true, message: 'If has played Volant is required', trigger: 'change' }],
        isPitch: [{ required: true, message: 'If has played Pitch is required', trigger: 'change' }],
      },
      downloadLoading: false,
      confirmLoading: false,
    }
  },
  created() {
    this.getList()
  },
  methods: {
    // Implmement edit in the table
    handleClick(row) {
      // 动态设置数据并通过这个数据判断显示方式
      if (row.isEdit) {
        this.$delete(row, 'isEdit')
      } else {
        this.$confirm('Note! You can only modify one row at a time, not multiple rows of data!', 'Warning', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(()=>{
          this.$set(row, 'isEdit', true);
        })
      }
    },
    handleSubmit(row) {
      this.$delete(row, 'isEdit')
      this.inlineUpdateData(row)
    },
    handleCancle(row) {
      this.getList()
    },
    ResetFilter() {
      this.getList()
    },
    getList() {
      this.listLoading = true

      getAllInfos().then(response => {
        // Just to simulate the time of the request
        console.log('response.data.infos:',response.data.infos)
        this.list = response.data.infos
        for (var i = 0; i < this.list.length; i++) {
          this.list[i].isAne = (this.list[i].isAne==true  || this.list[i].isAne == 1) ? 1 : 0  
          this.list[i].isVol = (this.list[i].isVol==true  || this.list[i].isVol == 1) ? 1 : 0  
          this.list[i].isPitch = (this.list[i].isPitch==true  || this.list[i].isPitch == 1) ? 1 : 0  
        }
        this.tmp_list =  response.data.infos
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    //TODO: Pagination
    handleFilter() {
      var new_array = []
      this.list = this.tmp_list
      console.log(this.listQuery, this.list)
      if (this.listQuery.name != undefined && this.listQuery.name != "" ) {
        for (var i = 0; i < this.list.length; i++) {
          if (this.list[i].name == this.listQuery.name) {
            new_array.push(this.list[i])
          }
        }
        this.list = new_array
        console.log('FILTER ACCORDING TO THE NAME.....')
      } else  {
        this.getList()
        this.$message({
          type:'info',
          message: 'NO FILTER'
        })
      }
      console.log('AFTER FILTERING, THE LIST IS: ', this.list)
    },
    ResetFilter() {
      this.getList()
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

    resetTemp() {
      this.temp = {
        id: undefined,
        name: '',
        isAne: 0,
        isVol: 0,
        isPitch: 0,
        score: 0,
        email: '',
        telephone: 'None',
        loc: 'None',
        pays: ''
      }
    },

    handleCreate() {
      console.log('dialogStatus:', this.dialogStatus)
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          addInfo(this.temp).then(() => {
            this.confirmLoading = true
            this.dialogFormVisible = false
            this.confirmLoading = false
            this.$notify({
              title: 'Success',
              message: 'Created Successfully',
              type: 'success',
              duration: 2000
            })
            this.getList()
          }).catch( err => {
            console.error(err)
          })
        }
      })
    },
    handleUpdate(row) {
      console.log('dialogStatus:', this.dialogStatus)
      this.temp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'Update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          tempData.isAne = parseInt(tempData.isAne)
          tempData.isVol = parseInt(tempData.isVol)
          tempData.isPitch = parseInt(tempData.isPitch)
          tempData.score = parseInt(tempData.score)
          console.log(tempData)
          updateInfo(tempData).then(() => {
            this.confirmLoading = true
            this.dialogFormVisible = false
            this.confirmLoading = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          }).catch(err => {
            console.error(err)
            this.$notify({
              title: 'Failed to update',
              message: 'Update Failed' + err,
              type: 'warning',
              duration: 2000
            })
          })
        }
      })
    },
    inlineUpdateData(row) {
      const tempData = Object.assign({}, row)
      tempData.isAne = parseInt(tempData.isAne)
      tempData.isVol = parseInt(tempData.isVol)
      tempData.isPitch = parseInt(tempData.isPitch)
      tempData.score = parseInt(tempData.score)
      console.log('TEMPDATA:', tempData)
      updateInfo(tempData).then(() => {
        this.confirmLoading = true
        this.dialogFormVisible = false
        this.confirmLoading = false
        this.$notify({
          title: 'Success',
          message: 'Update Successfully',
          type: 'success',
          duration: 2000
        })
      }).catch(err => {
        console.error(err)
        this.$notify({
          title: 'Failed to update',
          message: 'Update Failed' + err,
          type: 'warning',
          duration: 2000
        })
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
      deleteInfo(index).then(() => {
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
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['ID', 'name', 'has Ane', 'has Pitch', 'has Volant', 'Score', 'Email', 'Tel', 'Country']
        const filterVal = ['id', 'name', 'isAne', 'isPitch', 'isVol', 'score', 'email', 'telephone', 'pays']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'Users table'
        })
        this.downloadLoading = false
      })
    },
    formatJson(filterVal) {
      return this.list.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
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