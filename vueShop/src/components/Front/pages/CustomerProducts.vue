<template>
  <div>
    <loading :active.sync="isLoading"></loading>
    <!-- <div class="ml-0 ">
      <div class="toc-entry row"><a>全部商品</a></div>
      <div class="toc-item row"><a>肉類</a></div>
      <div class="toc-item row"><a>魚類</a></div>
      <div class="toc-item row"><a>蔬菜</a></div>
    </div> -->
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/home/customer_products/全部">首頁</router-link></li>
        <li class="breadcrumb-item active" aria-current="page"  v-if="this.$route.params.category !== '全部'">{{ this.$route.params.category }}</li>
        <li class="breadcrumb-item active" aria-current="page" v-else>全部</li>
      </ol>
    </nav>
    <div class="row mt4" style="top:200px">
      <div class="col-md-4 mb-4" v-for="item in toggleProducts" :key="item.id">
        <div class="card border-0 shadow-sm">
          <div style="height: 150px; background-size: cover; background-position: center"
            :style="{backgroundImage: `url(${item.imageUrl})`}">
          </div>
          <div class="card-body">
            <span class="badge badge-secondary float-right ml-2">{{ item.category }}</span>
            <h5 class="card-title">
              <a href="#" class="text-dark">{{ item.title }}</a>
            </h5>
            <p class="card-text">{{ item.content }}</p>
            <div class="d-flex justify-content-between align-items-baseline">
              <div class="h5" v-if="!item.price">{{ item.origin_price }} 元</div>
              <del class="h6" v-if="item.price">原價 {{ item.origin_price }} 元</del>
              <div class="h5" v-if="item.price">現在只要 {{ item.price }} 元</div>
            </div>
          </div>
          <div class="card-footer d-flex">
            <button type="button" class="btn btn-outline-secondary btn-sm"
              @click="getProduct(item.id)">
              <i class="fas fa-spinner fa-spin" v-if="status.loadingItem === item.id"></i>
              查看更多
            </button>
            <button type="button" class="btn btn-outline-danger btn-sm ml-auto" @click="addCart(item.id)">
              <i class="fas fa-spinner fa-spin" v-if="status.loadingItem === item.id"></i>
              加到購物車
            </button>
          </div>
        </div>
      </div>
    </div>
    <Pagination :pagination="pagination" @emitPage="getToggleProductList"
      v-if="pagination.current_page !== 0"></Pagination>
    
    <!-- Modal -->
    <div class="modal fade" id="adModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">歡慶開幕</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <span class="h2">現在只要輸入優惠碼 [</span> 
            <span class="text-warning h2"> food </span> 
            <span class="h2">] </span><br />
            <span class="h2">就享有</span> 
            <span class="text-success h2">80%</span> 
            <span class="h2">優惠</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';
import Pagination from '../../Pagination';

export default { 
  data() {
    return {
      products: [],
      product: {},
      categoryProducts: [],
      toggleProducts: [],
      pagination: {},
      status: {
        loadingItem: '',
      },
      isLoading: false,
    };
  },
  components: {
    Pagination,
  },
  methods: {
    getProducts() {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/products/all`;
      vm.isLoading = true;
      this.$http.get(api).then((response) => {
        vm.products = response.data.products;
        console.log(response);
        vm.isLoading = false;
        // vm.pagination = response.data.pagination;
        vm.getCategoryProducts();
      });
    },
    getCategoryProducts() {
      const vm = this;
      let list = vm.$route.params.category;
      if (list === '全部') {
        vm.categoryProducts = vm.products.filter(item => item.is_enabled == 1);
      } else {
        vm.categoryProducts = vm.products.filter(item => item.category === list && item.is_enabled == 1);
        console.log(vm.categoryProducts);
      };
      vm.getToggleProductList(1);
    },
    getToggleProductList(page) {
      const vm = this;
      let startItem = (page - 1) * 9,
          endItem = page * 9,
          paginationData = {};
      vm.toggleProducts = vm.categoryProducts.slice(startItem, endItem);
      paginationData.total_pages = Math.ceil(vm.categoryProducts.length / 9);
      paginationData.current_page = page;
      paginationData.current_page < paginationData.total_pages ? paginationData.has_next = true : paginationData
          .has_next = false;
      paginationData.current_page == 1 ? paginationData.has_pre = false : paginationData.has_pre = true;
      vm.pagination = paginationData;
    },
    getProduct(id) {
      const vm = this;
      vm.$router.push(`/home/product_detail/${id}`);
    },
    addCart(id, qty = 1){
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/cart`;
      vm.status.loadingItem = id;
      const cart = {
        product_id: id,
        qty
      };
      this.$http.post(api, { data: cart}).then((response) => {
        console.log(response);
        vm.product = response.data.data.product;
        vm.$bus.$emit('message:push', '新增商品'+ vm.product.title, 'success');
        vm.status.loadingItem = '';
        vm.$bus.$emit('cart:updete');
        $('#productModal').modal('hide');
      });
    },
    adModal() {
      $('#adModal').modal('show');
    },
  },
  watch: {
      '$route'() {
        this.getCategoryProducts();
      }
    },
  created() {
    this.getProducts();
    if(this.$route.params.category === '全部') {
      setTimeout(() => {
        this.adModal();
      }, 1000);
    }
  },
};
</script>

<style lang="scss">
  .breadcrumb{
    background-color: transparent;
  }
</style>