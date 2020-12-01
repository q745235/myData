<template>
  <div>
    <ul id="slide">
      <li><router-link to="/home/customer_products/全部">全部</router-link></li>
      <li><router-link to="/home/customer_products/肉品">肉品</router-link></li>
      <li><router-link to="/home/customer_products/鮮魚">鮮魚</router-link></li>
      <li><router-link to="/home/customer_products/蔬菜">蔬菜</router-link></li>
    </ul>
  </div>
</template>

<style lang="scss">
  #slide {
    position: sticky;
    left: 10px;
    top: 30px;
    padding-top: 20px;
  }
</style>