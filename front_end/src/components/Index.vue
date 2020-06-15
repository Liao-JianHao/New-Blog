<template>
      <div>
        <div class="container-1">
          <input type="search" id="search" placeholder="Search..." />
        </div>

        <div class="top_image" id="top_image" :style="{backgroundImage: 'url(http://' + img + ')'}">

          <div class="page1">

              <div class="nav">
                <h1>Mr&nbsp;.&nbsp;C</h1>
                <p>滴水穿石，非一日之功</p>
                <a href="#" id="resume">个人<span>简历</span></a>
              </div>

            <a href="#" id="next"></a>
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
      flag:true,
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
  
 
// .box{
//   margin: 10px auto;
//   width: 300px;
//   height: 50px;
// }






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

    .page1 {
    position:relative;
    display: table-cell;
    vertical-align: middle;
    width: 100%;
    height: 100%;
    position: relative;
    z-index: 1;
  }

  .page1 .nav {
    text-align: center;
    color: #9d968e; // 字体颜色
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


  
  #resume{
    text-decoration:none;
    font-size: 20px;
    color: #fefefe;
    background-color: #010101;
    padding: 7px;
    letter-spacing : 2px;
    border-radius: 5px;
  }
  #resume span{
    color: #010101;
    background-color: #fd9906;
    border-radius: 5px;
    padding: 1px;
  }

  #resume:hover {
    color: #010101;
    background-color: #fd9906;
    border-radius: 5px;
    transition: background .55s ease;
    -webkit-transition: background .55s ease;
    -moz-transition: background .55s ease;
    -ms-transition: background .55s ease;
    -o-transition: background .55s ease;
  }
  #resume span:hover{
    color: #fefefe;
    background-color: #010101;
    transition: background 2.55s ease;
    -webkit-transition: background 2.55s ease;
    -moz-transition: background 2.55s ease;
    -ms-transition: background 2.55s ease;
    -o-transition: background 2.55s ease;
  }

  #next{
    display: block;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    position: absolute;
    bottom: 30px;
    left: 50%;
    margin-left: -25px!important;
    z-index: 0;
    -webkit-transition: all .5s ease-out;
    transition: all .5s ease-out;
    cursor: pointer;
  }

  #next:after {
    font-family: FontAwesome;
    content: "∨";
    color: #fff;
    font-size: 2rem;
    display: table;
    margin: 0 auto;
}
#next:hover {
  border-radius: 50%;
  background-color: #fd9906;
  -webkit-transition: background 1.55s ease;
  -moz-transition: background 1.55s ease;
  -ms-transition: background 1.55s ease;
  -o-transition: background 1.55s ease;
  transition: background 1.55s ease;
}



.container-1{
  position: fixed;
  width: 20px;
  border-radius: 50%;
  cursor: pointer;
  background-color: #fff;
  overflow: hidden;
  z-index: 102;
}

.container-1 input#search{
  position: fixed;
  width: 300px;
  height: 50px;
  background: #2b303b;
  border: none;
  font-size: 10pt;
  float: left;
  color: #63717f;
  padding-left: 45px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  
  -webkit-transition: background 1.55s ease;
  -moz-transition: background 1.55s ease;
  -ms-transition: background 1.55s ease;
  -o-transition: background 1.55s ease;
  transition: background 1.55s ease;
}

.container-1 input#search::-webkit-input-placeholder {
   color: #65737e;
}
 
.container-1 input#search:-moz-placeholder { /* Firefox 18- */
   color: #65737e;  
}
 
.container-1 input#search::-moz-placeholder {  /* Firefox 19+ */
   color: #65737e;  
}
 
.container-1 input#search:-ms-input-placeholder {  
   color: #65737e;  
}

.container-1 input#search:hover, .container-1 input#search:focus, .container-1 input#search:active{
    outline:none;
    background: #ffffff;
  }

  
</style>