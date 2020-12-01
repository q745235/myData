<template>
  <div>
    <button class="btn btn-cart" data-toggle="dropdown" id="cart-button">
      <div>
         <i class="fas fa-shopping-cart text-dark fa-2x" id="cart"></i>
        <span class="badge badge-pill badge-danger" id="badge">{{cartLen}}</span>
      </div>
    </button>
    <div class="dropdown-menu dropdown-menu-right">
      <loading :active.sync="isLoading"></loading>
      <table class="table table-hover table-sm" style="margin-bottom:0;">
        <thead>
            <th class="thead"></th>
            <th class="thead">品名</th>
            <th class="thead1">數量</th>
            <th class="thead">單價</th>
          </thead>
      </table>
      <div class="align-middle text-center text-success" v-if="!cartLen"><p>您尚未購買商品</p></div>
      <div class="align-middle" id="cart-scroll" v-else>
        <table class="table table-hover table-sm">
          <tbody> 
            <tr v-for="item in cart.carts" :key="item.id">
              <td class="align-middle">
                <button type="button" class="btn btn-outline-danger btn-sm"
                  @click="removeCartItem(item.id)">
                  <i class="far fa-trash-alt"></i>
                </button>
              </td>
              <td class="align-middle">
                {{ item.product.title }}
                <div class="text-success" v-if="item.coupon">
                  已優惠
                </div>
              </td>
              <td class="align-middle">{{ item.qty }}/{{ item.product.unit }}</td>
              <td class="align-middle text-right">{{ item.final_total }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="text-center" v-if="cartLen">
        <div class="d-flex flex-row justify-content-end">
          <div class="text-right cart-flex">總計</div>
          <div class="text-right cart-flex">{{ cart.total }}</div>
        </div>
        <div class="d-flex flex-row justify-content-end" v-if="cart.final_total !== cart.total">
          <div class="text-right cart-flex text-success">折扣價</div>
          <div class="text-right cart-flex text-success">{{ Math.ceil(cart.final_total) }}</div>
        </div>
        <button class="btn btn-danger" @click.prevent="toPay">送出訂單</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['cartData'],
  data() {
    return{
      cart: {},
      isLoading: false,
      cartLen: 0,
    };
  },
  methods: {
    getCart() {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/cart`;
      vm.isLoading = true;
      this.$http.get(api).then((response) => {
        vm.cart = response.data.data;
        vm.cartLen = vm.cart.carts.length;
        console.log(response);
        vm.isLoading = false;
      });
    },
    removeCartItem(id) {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/cart/${id}`;
      vm.isLoading = true;
      this.$http.delete(api).then(() => {
        vm.getCart();
        vm.isLoading = false;
        vm.$bus.$emit('message:push', '已刪除商品', 'success');
        vm.$bus.$emit('cart:updete');
      });
    },
    toPay() {
      this.$router.push(`/home/user_order`);
    },
  },
  created() {
    this.getCart();
    const vm = this;
    vm.$bus.$on('cart:updete', ()=>{
      vm.getCart();
    });
  },
}
</script>

<style lang="scss">
  .thead {
    padding-left: 20px !important;
  }
  .thead1 {
    padding-left: 50px !important;
  }
  #badge {
    top: -30px;
    right: -15px;
  }
  #cart {
    position: relative;
    top: 10px;
  }
  .dropdown-menu {
    margin-top: 0px;
    padding: 0px;
  }
  #cart-button {
    padding: 0px;
    width: 50px;
  }
  #cart-scroll {
    max-height: 300px;
    overflow: auto;
  }
  .cart-flex {
    padding-right: 20px;
    padding-bottom: 10px;
  }
</style>