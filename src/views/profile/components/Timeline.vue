<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of timeline" :key="index" :timestamp="item.timestamp" placement="top">
        <el-card>
          <h4>{{ item.title }}</h4>
          <p>{{ item.content }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timeline: [
        {
          timestamp: '2021/5/14',
          title: 'Finish the user table',
          content: 'LinHaonan committed 2021/5/14 20:46'
        },
        {
          timestamp: '2021/5/13',
          title: 'Finish the Login part',
          content: 'LinHaonan committed 2019/5/13 17:36'
        },
        {
          timestamp: '2021/5/11',
          title: 'Build Template, Initialize',
          content: 'LinHaonan committed 2021/5/12 18:53'
        }
      ]
    }
  }
}
</script>
