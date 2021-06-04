<template>
  <el-row :gutter="40" class="panel-group">
    <el-col :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('zhurou_jiaozi')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            猪肉饺子
          </div>
          <count-to :start-val="0" :end-val="102400" :duration="2600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('niurou_jiaozi')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            牛肉饺子
          </div>
          <count-to :start-val="0" :end-val="81212" :duration="3000" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('jidan_jiaozi')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            鸡蛋饺子
          </div>
          <count-to :start-val="0" :end-val="9280" :duration="3200" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('qita_jiaozi')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            其他饺子
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('difang_tese_mianshi')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            特色面食
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('huntun')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            美味馄饨
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('zongzi')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            粽子
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="7" :sm="5" :lg="3" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('xinpin')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            尝鲜新品
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="8" :sm="6" :lg="4" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('jiachang_8')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            家常菜8欧系列
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="8" :sm="6" :lg="4" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('jiachang_6')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            家常菜6欧系列
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="8" :sm="6" :lg="4" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('jiachang_5')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            家常菜5欧系列
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="8" :sm="6" :lg="4" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('jiachang_16')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            家常菜16欧系列
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="8" :sm="6" :lg="4" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('jiachang_12')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            家常菜12欧系列
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
    <el-col  :xs="8" :sm="6" :lg="4" class="card-panel-col">
      <div class="card-panel" @click="handleSetLineChartData('jiachang_10')">
        <div class="card-panel-description">
          <div class="card-panel-text">
            家常菜10欧系列
          </div>
          <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  components: {
    CountTo
  },
  methods: {
    handleSetLineChartData(type) {
      this.$emit('handleSetLineChartData', type)
    }
  }
}
</script>

<style lang="scss" scoped>
.panel-group {
  margin-top: 10px;

  .card-panel-col {
    margin-bottom: 20px;
  }

  .card-panel {
    height: 8vw;
    cursor: pointer;
    font-size: 2vw;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);

    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }

      .icon-people {
        background: #40c9c6;
      }

      .icon-message {
        background: #36a3f7;
      }

      .icon-money {
        background: #f4516c;
      }

      .icon-shopping {
        background: #34bfa3
      }
    }

    .icon-people {
      color: #40c9c6;
    }

    .icon-message {
      color: #36a3f7;
    }

    .icon-money {
      color: #f4516c;
    }

    .icon-shopping {
      color: #34bfa3
    }

    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;

      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 16px;
        margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 1.5vw;
      }
    }
  }
}

@media (max-width: 900px)  {
  .card-panel-num {
    display: none;
  }
}

@media (max-width:550px) {
  .card-panel-description {
    display: none;
  }

  .card-panel-icon-wrapper {
    float: none !important;
    width: 100%;
    height: 100%;
    margin: 0 !important;

    .svg-icon {
      display: block;
      margin: 14px auto !important;
      float: none !important;
    }
  }
}
</style>
