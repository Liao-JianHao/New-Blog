<template>
      <div>
        <div class="top_image" id="top_image" :style="{backgroundImage: 'url(http://' + img + ')'}">

            <div class="page1">
              <div class="nav wow zoomIn animated" data-wow-duration="2s" style="visibility: visible; animation-duration: 2s; animation-name: zoomIn;">
                <h1>Mr&nbsp;.&nbsp;C</h1>
                <p>滴水穿石，非一日之功</p>
              </div>
            </div>

        </div>
        
        
      </div>
      
      
</template>

<script>
import axios from 'axios'
export default {
  name: "Index",
  data() {
    return {
      img: "192.168.47.132:8888/group1/M00/00/00/wKgvhF7SWWGAR5lFAAENFHx2erM988.jpg",
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
      // console.log(res);
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

  .top_image{
    overflow: hidden;
    display: table;
    table-layout: fixed;
    width: 100%;
    position: relative;
    padding: 100px 0;
  }

  #top_image::after{
    content: "";
    position: absolute; // 蒙板
    top: 0;
    left: 0;
    z-index: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,.5);
  }

  .page1 .nav {
    text-align: center;
    color: #9d968e; // 字体颜色
  }
  .zoomIn {
    -webkit-animation-name: zoomIn;
    animation-name: zoomIn;
  }
  .animated {
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
  }
  .page1 p {
    letter-spacing: 10px;
    margin: 20px 0;
    font-size: 2em;
    text-shadow: 
    	  	0 -1px 0 #858585,
              
               
               0 1px 10px rgba(0,0,0,.6),
               0 6px 1px rgba(0,0,0,.1),
               0 0 5px rgba(0,0,0,.2),
               0 1px 3px rgba(0,0,0,.3),
               0 3px 5px rgba(0,0,0,.2),
               0 7px 10px rgba(0,0,0,.25),
               0 15px 10px rgba(0,0,0,.2),
               0 25px 15px rgba(0,0,0,.15);
  }

  .page1 h1{
    font-size: 4em;
    text-shadow: 
    	  	0 -1px 0 #858585,
              
               
               0 1px 10px rgba(0,0,0,.6),
               0 6px 1px rgba(0,0,0,.1),
               0 0 5px rgba(0,0,0,.2),
               0 1px 3px rgba(0,0,0,.3),
               0 3px 5px rgba(0,0,0,.2),
               0 7px 10px rgba(0,0,0,.25),
               0 15px 10px rgba(0,0,0,.2),
               0 25px 15px rgba(0,0,0,.15);
  }

  .page1 {
    position:relative;
    display: table-cell;
    vertical-align: middle;
    width: 100%;
    height: 100%;
    position: relative;
    z-index: 1;
  }
  
</style>