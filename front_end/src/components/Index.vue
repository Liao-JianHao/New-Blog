<template>
      <div id="top_image" :style="{backgroundImage: 'url(http://' + img + ')'}"></div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      img: null,
    }
  },
  created:function () {
    this.getImage()
  },
  methods:{
    getImage(){
      axios.get('/api/index/image_url')
    .then(res => {
      this.img = res.data.image_url;
      console.log(res);
    })
    .catch(error => {
      console.log(error);
    });
    }
  }
}




</script>

<style lang="less" scoped>
  #top_image{
    background-size: cover;
    height: 100vh;
    padding: 0;
    background-color: transparent;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    overflow: hidden;
    display: table;
    table-layout: fixed;
    width: 100%;
    position: relative;
  }
</style>