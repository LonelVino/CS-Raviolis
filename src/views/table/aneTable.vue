<template>
  <div class="app-container">
    <el-collapse v-model="activeNames" @change="handleChange"  style="font-weight: bolder">
      <el-collapse-item>
        <template slot="title" style="font-weight:bolder;">
          <i class="el-icon-arrow-left"></i> HINTS OF ANE ROUGE TABLE<i class="el-icon-arrow-right"></i>  <i class="el-icon-star-on"></i>
        </template>
        <el-collapse-item title="General Hints of Usage" name="1" style="font-weight: bolder">
          <div> <p class="note-txt">1.When modifying the value of 'isPart', 'isFini', <b>0 infers to 'No'</b>, <b>1 infers to 'Yes' </b></p></div>
          <div>      <p class="note-txt"> 2.It's available to modify the value of the table by double-clicking the content of the table</p>  </div>
          <div>      <p class="note-txt"> 3.But while doing so, you can only modify one row at a time, editing multiple rows of data is not suggested and allowed.</p>  </div>
        </el-collapse-item>
        <el-collapse-item title="Usage of the 3 ANE ACTION BUTTONS" name="2" style="font-weight: bolder">
          <div class="button-hints" style="display:flex; flex-direction: row; justify-content: space-around;">
            <div><el-button type="success" style='padding: -8px 0'>start</el-button> <i class="el-icon-right"></i><el-tag type='info'> Start the timer.</el-tag></div>
            <div><el-button type="danger" style='padding: -8px 0'>End</el-button> <i class="el-icon-right"></i><el-tag type='info'> End the timer.</el-tag></div>
            <div><el-button type="primary" style='padding: -8px 0'>Next</el-button> <i class="el-icon-right"></i><el-tag type='info'> Incrememt the hints step. (From level 1 -> level 6)</el-tag></div>
          </div>
        </el-collapse-item>
        <el-collapse-item title="Usage of the 5 ACTION BUTTONS" name="3" style="font-weight: bolder">
          <div class="button-hints" style="display:flex; flex-direction: row; justify-content: flex-start; margin: 10px 0;">
            <div style="margin: 0 0.3vw"><el-button type="primary" style='padding: -8px 0'>submit</el-button> <i class="el-icon-right"></i><el-tag type='info'> Submit the information of this row.</el-tag></div>
            <div style="margin: 0 0.3vw"><el-button type="warning" style='padding: -8px 0'>cancle</el-button> <i class="el-icon-right"></i><el-tag type='info'> Cancle the submit.</el-tag></div>
            <div style="margin: 0 0.3vw"><el-button type="info" style='padding: -8px 0'>Edit in Dialog</el-button> <i class="el-icon-right"></i><el-tag type='info'> ALlow to modify the data by opening form dialog. </el-tag></div>
          </div>
          <div class="button-hints" style="display:flex; flex-direction: row; justify-content: flex-start;  margin: 10px 0;">
            <div style="margin: 0 0.3vw"><el-button type="danger" disabled style='padding: -8px 0'>delete</el-button> <i class="el-icon-right"></i><el-tag type='info'> Delete the information of this row, not allowed here.</el-tag></div>
            <div style="margin: 0 0.3vw"><el-button type="warning" style='padding: -8px 0'>restart</el-button> <i class="el-icon-right"></i><el-tag type='info'> if one wants more chances to play this game again..... </el-tag></div>
          </div>
        </el-collapse-item>
      </el-collapse-item>  
  </el-collapse>
    <el-divider></el-divider>
    
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.isFini" placeholder="isFini" clearable style="width: 90px" class="filter-item">
        <el-option v-for="item in isFiniOptions" :key="item" :label="item"  :value="item" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-refresh-right" @click="ResetFilter">
        Reset
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate" disabled>
        Add
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        Export
      </el-button>
      <el-checkbox v-model="showReviewer" class="filter-item" style="margin-left:15px;" @change="tableKey=tableKey+1">
        show comments
      </el-checkbox>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange"
    >
      <el-table-column label="ID" prop="id" align="center" width="80" >
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="isPart" class-name="status-col" align="center" width="100">
        <template slot-scope="scope">
         <el-switch
            v-model="scope.row.isPart"
            :active-value="1"
            :inactive-value="0"
            active-color="#02538C"
            inactive-color="#B9B9B9"
            @change="changeSwitch(scope.row)"
            v-bind:disabled="scope.row.isPart"
          />
        </template>
      </el-table-column>
      <el-table-column label="hasInd" class-name="status-col" align="center" width="100">
        <template slot-scope="scope">
         <el-switch
            v-model="scope.row.hasInd"
            :active-value="1"
            :inactive-value="0"
            active-color="#02538C"
            inactive-color="#B9B9B9"
            @change="changeSwitch(scope.row)"
            v-bind:disabled="!scope.row.isPart || scope.row.isFini"
          />
        </template>
      </el-table-column>
      <el-table-column label="isFini" class-name="status-col" align="center" width="100">
        <template slot-scope="scope">
          <el-switch
            v-model="scope.row.isFini"
            :active-value="1"
            :inactive-value="0"
            active-color="#02538C"
            inactive-color="#B9B9B9"
            @change="changeSwitchFini(scope.row)"
            v-bind:disabled="scope.row.isFini || scope.row.status == 0 || scope.row.status == 2"
          />
        </template>
      </el-table-column>
      <el-table-column label="Step" class-name="status-col" align="center" width="100">
        <template slot-scope="scope">
          <span>{{scope.row.step}}</span>
        </template>
      </el-table-column>
      <el-table-column label="Time" class-name="status-col" align="center" width="100">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.time}} s</div>
          <div v-else>
            <el-input v-bind:disabled="scope.row.isFini" v-model="scope.row.time" type='number' @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Score" width="100px" sortable="custom" align="center">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.a_score}}</div>
          <div v-else>
            <el-input v-bind:disabled="scope.row.isFini" v-model="scope.row.a_score" type='number' @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column v-if="showReviewer" label="Comments" width="200">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.comment}}</div>
          <div v-else>
            <el-input v-bind:disabled="scope.row.isFini" v-model="scope.row.comment" @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>

     <el-table-column label="ANE-Actions" align="center" width="230" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="success" size="mini" @click="handleStart(row)" v-bind:disabled="row.isFini || row.isPart == 0 || row.status == 1 || row.status == 2">
            Start
          </el-button>
          <el-button type="primary" size="mini" @click="handleNextStep(row)" v-bind:disabled="row.isFini || row.isPart == 0 || row.status == 2">
            Next
          </el-button>
          <el-button type="danger" size="mini" @click="handleEnd(row)" v-bind:disabled="row.isFini || row.status == 0 || row.status == 2">
            End
          </el-button>
        </template>
     </el-table-column>
     <el-table-column label="Actions" align="center" width="420" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleSubmit(row)" v-bind:disabled="row.isFreeze">
            Submit
          </el-button>
          <el-button type="warning" size="mini" @click="handleCancle(row)" v-bind:disabled="row.isFreeze">
            Cancle
          </el-button>
          <el-button type="info" size="mini" @click="handleUpdate(row)" v-bind:disabled="row.isFreeze">
            Edit in Dialog
          </el-button>
          <el-button v-if="row.status!='deleted'" size="mini" type="danger" disabled @click="confirmDelete(row.id)">
            Delete
          </el-button>
          <el-button type="warning" size="mini"  @click="handleRestart(row)">
            Restart
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="80px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name" required>
          <el-input v-model="temp.name" disabled />
        </el-form-item>
        <el-form-item label="Have Participated?">
          <el-switch v-model="temp.isPart"></el-switch>
        </el-form-item>
        <el-form-item label="Has Indice?">
          <el-switch v-model="temp.hasInd"></el-switch>
        </el-form-item>
        <el-form-item label="Have Fininshed?">
          <el-switch v-model="temp.isFini"></el-switch>
        </el-form-item>
        <el-form-item label="Time" prop="time"  required>
          <el-input  type="number" v-model="temp.time" />
        </el-form-item>
        <el-form-item label="Step" required>
          <el-input  type="number" v-model="temp.step" />
        </el-form-item>
        <el-form-item label="Score" prop="a_score" required>
          <el-input  type="number" v-model="temp.a_score" />
        </el-form-item>
        <el-form-item label="Comment">
          <el-input  v-model="temp.comment" />
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import {getScore, getAllScores, addScore, updateScore, deleteScore} from '@/api/ane'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination


export default {
  name: 'AneTable',
  components: { Pagination },
  directives: { waves },

  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    },
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
        isFini: undefined,
        name: undefined,
      },

      isFiniOptions: ['true', 'false'],
      showReviewer: false,
      temp: {
        id: undefined,
        name: 'None',
        isPart: 0,
        hasInd: 0,
        isFini: 0,
        isFreeze: 0,
        a_score: 0,
        time: 0,
        start_time: undefined,
        end_time: undefined,
        status: 0,  // 0: default, 1: start, 2:end
        step: 0,
        comment: '',
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
        time: [{  required: true, message: 'time is required and should be a number', trigger: 'blur' }],
        a_score: [{ required: true, message: 'score is required  and should be a number', trigger: 'blur' }]
      },
      downloadLoading: false
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


    getList() {
      this.listLoading = true
      getAllScores().then(response => {
        // Just to simulate the time of the request
        this.list = response.data.infos
        for (var i = 0; i < this.list.length; i++) {
          this.list[i].isPart = (this.list[i].isPart==true  || this.list[i].isPart == 1) ? 1 : 0  
          this.list[i].hasInd = (this.list[i].hasInd==true  || this.list[i].hasInd == 1) ? 1 : 0  
          this.list[i].isFini = (this.list[i].isFini==true  || this.list[i].isFini == 1) ? 1 : 0  
          this.list[i].isFreeze = (this.list[i].isFreeze==true  || this.list[i].isFreeze == 1) ? 1 : 0  
        }
        
        this.tmp_list = this.list
        console.log(this.list)
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
      if (this.listQuery.isFini != undefined  && (this.listQuery.name != undefined && this.listQuery.name != "" )) {
        for (var i = 0; i < this.list.length; i++) {
          var cor2isFini = (this.list[i].isFini === true && this.listQuery.isFini == 'true') || (this.list[i].isFini === false && this.listQuery.isFini == 'false')
          if ((this.list[i].name == this.listQuery.name) && cor2isFini) {
            new_array.push(this.list[i])
          }
        }
        this.list = new_array
        console.log('FILTER ACCORDING TO BOTH THE NAME AND ISFINI.....')        
      } else if (this.listQuery.name != undefined && this.listQuery.name != "" ) {
        for (var i = 0; i < this.list.length; i++) {
          if (this.list[i].name == this.listQuery.name) {
            new_array.push(this.list[i])
          }
        }
        this.list = new_array
        console.log('FILTER ACCORDING TO THE NAME.....')
      } else if (this.listQuery.isFini != undefined) {
        for (var i = 0; i < this.list.length; i++) {
          if ((this.list[i].isFini == true && this.listQuery.isFini == 'true') || (this.list[i].isFini == false && this.listQuery.isFini == 'false')) {
            new_array.push(this.list[i])
          } 
        }
        this.list = new_array
        console.log('FILTER ACCORDING TO ISFINI.....')
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

    // GAME PART -- START STOP END
    handleStart(row) {
      row.status = 1
      row.start_time = new Date()
      this.$notify({
        title: 'Timer Starts',
        message: 'Timer starts succcessully!! You can end timer then.',
        type: 'info',
        duration: 2000
      })
    },
    handleNextStep(row) {
      row.step += 1
      if (row.step == 6) {
        this.handleEnd(row)
      }
    },
    handleEnd(row) {
      row.status = 2
      row.isFini = 1
      row.end_time = new Date()
      row.time = (row.end_time - row.start_time)/1000
      this.$notify({
        title: 'Timer ends',
        message: 'Timer ends succcessully!! The The duration is ' + row.time +' seconds. You could submit the data now.',
        type: 'success',
        duration: 5000
      })
    },

    resetTemp() {
      this.temp = {
        id: undefined,
        name: 'None',
        isPart: 0,
        hasInd: 0,
        isFini: 0,
        isFreeze: 0,
        a_score: 0,
        time: 0,
        start_time: new Date(),
        end_time: new Date(),
        status: 0,  // 0: default, 1: start, 2:end
        step: 0,
        comment: '',
      }
    },
    handleCreate() {
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
          console.log('this.temp.isPart, this.temp.isFini: ', this.temp.isPart, this.temp.isFini)
          // this.temp.isPart = (this.temp.isPart == true  || tempData.isFini == 1) ? 1 : 0 
          // this.temp.isFini = (this.temp.isFini == true  || tempData.isFini == 1) ? 1 : 0 
          this.temp.time = parseInt(this.temp.time)
          this.temp.a_score = parseInt(this.temp.a_score)
          addScore(this.temp).then(response => {
            // Just to simulate the time of the request
            console.log(response)
            this.$message({
              message: 'ADD ' + response.data.name + "'s Score Successfully!",
              type: 'success'
            })
            this.listLoading = true
            this.dialogFormVisible = false
            setTimeout(() => {
              this.getList()
            }, 1.5 * 1000)
          }).catch (e => {
            console.error(e)
            this.$message({
              message: 'ADD Score failed!',
              type: 'danger'
            })
          })
          this.resetTemp()
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$confirm('Are you sure to submit? Once you submitted, the operation cannot be undone!', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.confirmUpdate()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Update cancled'
          });          
        });
    },
    confirmUpdate() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          console.log('this.temp.isPart, this.temp.isFini: ', this.temp.isPart, this.temp.isFini)
          const tempData = Object.assign({}, this.temp)
          tempData.isPart = (tempData.isPart == true || tempData.isPart == 1) ? 1 : 0           
          tempData.isFini = (tempData.isFini == true || tempData.isFini == 1) ? 1 : 0 
          tempData.time = parseInt(tempData.time)
          tempData.a_score = parseInt(tempData.a_score)
          tempData.isFreeze = 1 
          updateScore(tempData).then(response => {
            this.$message({
              message: 'UPDATE ' + response.data.name + "'s Score Successfully!",
              type: 'success'
            })
            this.listLoading = true
            this.dialogFormVisible = false
            setTimeout(() => {
              this.getList()
            }, 1.5 * 1000)
          }).catch (e => {
            console.error(e)
            this.$message({
              message: 'UPDATE Score failed!',
              type: 'danger'
            })
          })
        }
        this.resetTemp()
      })
    },
    inlineUpdateData(row) {
      this.$confirm('Are you sure to submit? Once you submitted, the operation cannot be undone! (If you want to modify the data, you have to restart the game!)', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          console.log('this.temp.isPart, this.temp.isFini: ', this.temp.isPart, this.temp.isFini)
          const tempData = Object.assign({}, row)
          tempData.isFini = parseInt(tempData.isFini)
          tempData.isFini = (tempData.isFini == true || tempData.isFini == 1) ? 1 : 0 
          tempData.time = parseInt(tempData.time)
          tempData.a_score = parseInt(tempData.a_score)
          tempData.isFreeze = 1 
          console.log('TEMPDATA:', tempData)
          updateScore(tempData).then(() => {
            this.confirmLoading = true
            this.dialogFormVisible = false
            this.confirmLoading = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
            this.getList()
          }).catch(err => {
            console.error(err)
            this.$notify({
              title: 'Failed to update',
              message: 'Update Failed' + err,
              type: 'warning',
              duration: 2000
            })
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Update cancled'
          });          
        });
      
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
      deleteScore(index).then(res => {
        this.$notify({
          title: 'Success',
          message: 'Delete Successfully',
          type: 'success',
          duration: 2000
        })
        this.getList()
      }).catch(e => {
        console.error(e)
        this.$message({
          type: 'danger',
          message: 'Delete failed, ' + e
        });      
      })
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['ID', 'name', 'has Participated?', 'has Finished?', 'Time', 'Score', 'Country', 'Comments']
        const filterVal = ['id', 'name','isPart', 'isFini', 'time', 'a_score', 'pays', 'comment']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'ane-rouge-table'
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
    changeSwitchFini(row) {
      if (row.isFini == 1) {
        row.status = 2
        row.end_time = new Date()
        row.time = (row.end_time - row.start_time)/1000
        this.$notify({
          title: 'Timer ends',
          message: 'Timer ends succcessully!! The The duration is ' + row.time +' seconds. You could submit the data now.',
          type: 'success',
          duration: 5000
        })
      }
    },
    handleRestart (row) {
      this.$confirm('Are you sure to restart? Once you restart, the data will be cleaned up!', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.resetTemp()
          const tempData = Object.assign({}, row)
          tempData.isFini = 0
          tempData.hasInd = 0      
          tempData.isPart = 0
          tempData.isFreeze = 0
          tempData.status = 0
          tempData.time = parseInt(tempData.time)
          tempData.a_score = parseInt(tempData.a_score)
          updateScore(tempData).then(() => {
            this.confirmLoading = true
            this.dialogFormVisible = false
            this.confirmLoading = false
            this.$notify({
              title: 'Success Restart',
              message: 'Restart Successfully',
              type: 'success',
              duration: 2000
            })
            this.getList()
          }).catch(err => {
            console.error(err)
            this.$notify({
              title: 'Failed to Restart',
              message: 'Restart Failed' + err,
              type: 'warning',
              duration: 2000
            })
          })
        })
    }
  }
}
</script>

<style scoped>

.note-txt {
  font-weight: bold;
  color:rgb(226, 134, 13);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 0.5vw;
  margin: 0.2vw;
  display: flex;
  justify-content: flex-start;
}
</style>