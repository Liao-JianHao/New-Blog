<template>
    <div id="blog">
        <router-view ></router-view>
    </div>
    
</template>

<script>


export default {
  name: 'App'
}
</script>

<style>
  #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width:100%;
  height:100%;
  }


  
  *{
    padding: 0;
    margin: 0;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
  }
  html,body {
    line-height: 24px;
    font: 14px Helvetica Neue,Helvetica,PingFang SC,\5FAE\8F6F\96C5\9ED1,Tahoma,Arial,sans-serif;
    user-select:none;  /* 文字禁止选中 */
    width:100%;
    height:100%;
  }
  div {
    display: block;
  }
  blockquote, body, button, dd, div, dl, dt, form, h1, h2, h3, h4, h5, h6, input, li, ol, p, pre, td, textarea, th, ul {
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
  }

  h1, h2, h3, h4, h5, h6 {
    font-weight: 400;
  }
  h1 {
    display: block;
    font-size: 2em;
    margin-block-start: 0.67em;
    margin-block-end: 0.67em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;

    font-family: "Arial", sans-serif;
    text-align: center;
    font-weight: bold;
  }
  p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
  }
  
  a, img{
    text-decoration: none;
    border: none;
  }

  ul{list-style:none}
  img{vertical-align:top;border:none}
  .clearf:after,
  .clearf:before{
      content:"";
      display:block;
      clear:both;
  }

</style>
