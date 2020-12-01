<template>
  <div>
    <loading :active.sync="isLoading"></loading>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/home/customer_products/全部">首頁</router-link></li>
        <li class="breadcrumb-item"><router-link :to="{ name: 'CustomerProducts', params: { category: product.category }}">{{ product.category }}</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">{{ product.title }}</li>
      </ol>
    </nav>

    <div class="row">
      <div class="modal-dialog col-lg-5 offset-lg-2"><img :src="product.imageUrl" class="img-fluid" alt=""></div>
      <div class="modal-dialog col-lg-5" role="document">
        <div class="modal-content border-0">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              {{ product.title }}
            </h5>
            <span class="badge badge-secondary float-right ml-2">{{ product.category }}</span>
          </div>
          <div class="modal-body">
            <blockquote class="blockquote mt-3">
              <p class="mb-0">{{ product.content }}</p>
              <footer class="blockquote-footer text-right">{{ product.description }}</footer>
            </blockquote>
            <div class="d-flex justify-content-between align-items-baseline">
              <div class="h5" v-if="!product.price">{{ product.origin_price }} 元</div>
              <del class="h6" v-if="product.price">原價 {{ product.origin_price }} 元</del>
              <div class="h5" v-if="product.price">現在只要 {{ product.price }} 元</div>
            </div>
            <select name="" class="form-control mt-3" v-model="product.num">
              <option :value="num" v-for="num in 10" :key="num">
                選購 {{ num }} {{ product.unit }}
              </option>
            </select>
          </div>
            <div class="card-footer d-flex">
            <div class="text-muted text-nowrap mr-3">
                小計 <strong>{{ product.num * product.price}}</strong> 元
              </div>
            <button type="button" class="btn btn-outline-danger btn-sm ml-auto"  @click="addCart(product.id, product.num)">
              <i class="fas fa-spinner fa-spin" v-if="status.loadingItem"></i>
              加到購物車
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';

export default {
  data() {
    return {
      product: {},
      productId: '',
      isLoading: false,
      status: {
        loadingItem: false,
      },
    };
  },
  methods: {
    getProduct(id) {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/product/${vm.productId}`;
      this.$http.get(api).then((response) => {
        vm.product = response.data.product;
        $('#productModal').modal('show');
        console.log(response);
        vm.product.num = 1;
      });
    },
    addCart(id, qty = 1){
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/cart`;
      const cart = {
        product_id: id,
        qty
      };
      vm.status.loadingItem = true;
      this.$http.post(api, { data: cart}).then((response) => {
        if (response.data.success) {
          console.log(response);
          vm.$bus.$emit('message:push', '新增商品'+ vm.product.title, 'success');
          vm.$bus.$emit('cart:updete');
          vm.status.loadingItem = false;
          vm.$router.push('/home/customer_products/全部'); //購買完回首頁
        } else {
          vm.$bus.$emit('message:push', response.data.messgae, 'danger');
          vm.status.loadingItem = false;
        };  
      });
    },
  },
  created() {
    this.productId = this.$route.params.productId;
    console.log(this.productId);
    this.getProduct();
  },
}
</script>

<style lang="scss">
  img {
    max-width: 300px;
    max-height: 300px;
  }
  .breadcrumb{
    background-color: transparent;
  }
</style>