<template>
  <div>
    <Banner></Banner>
    <Alert/>
    <div class="container-fluid">
      <Slide id="slide" class="left"/>
      <div class="row">
        <main  class="col-md-9 ml-sm-auto col-lg-10 px-4 view">
          <router-view/>
        </main>
      </div>
    </div>
    <Footer class="view"/>
  </div>
</template>

<script>
import Alert from '../AlertMessage';
import Banner from './Banner';
import Footer from './Footer';
import Slide from './Slide';

export default {
  components:{
    Alert,
    Banner,
    Footer,
    Slide,
  },
};
</script>

<style lang="scss">
  #slide {
    position: relative;
    top: 30px;
  }
  .left {
    float: left;
  }
  main {
    margin: 0 0 0 0;
  }
</style>