<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel" data-interval="10000">
      <div class="carousel-inner">
        <div class="carousel-item  active carousel-1 bg-cover">
        </div>
        <div class="carousel-item carousel-2 bg-cover">
        </div>
        <div class="carousel-item carousel-3 bg-cover">
        </div>
      </div>
      <Head id="head"/>
    </div>
  </div>
</template>
<script>
import Head from './Head';

export default {
  components:{
    Head,
  },
}


</script>

<style lang="scss" scoped>
  #head {
    position: absolute;
    top:0px;
    width: 100%;
  }

  #carouselExampleControls {
    position: relative;
    top: 0px;
  }
  .carousel-item {
    height: 300px;  
    width: 100%;
  }
  .carousel-1 {
    background-image: url('../../assets/img/banner1.jpg');
  }
  .carousel-2 {
    background-image: url('../../assets/img/banner2.jpg');
  }
  .carousel-3 {
    background-image: url('../../assets/img/banner3.jpg');
  }
  .bg-cover {
    background-position: center center ;
    background-size: cover;
  }
</style>