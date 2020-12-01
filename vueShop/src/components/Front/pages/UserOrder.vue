<template>
  <div>
    <div class="my-5 row justify-content-center">
      <form class="col-md-6">
        <table class="table">
          <thead>
            <th></th>
            <th>品名</th>
            <th>數量</th>
            <th>單價</th>
          </thead>
          <tbody v-if="cart">
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
                  已套用優惠券
                </div>
              </td>
              <td class="align-middle">{{ item.qty }}/{{ item.product.unit }}</td>
              <td class="align-middle text-right">{{ item.final_total }}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="3" class="text-right">總計</td>
              <td class="text-right">{{ cart.total }}</td>
            </tr>
            <tr v-if="cart.final_total !== cart.total">
              <td colspan="3" class="text-right text-success">折扣價</td>
              <td class="text-right text-success">{{ Math.ceil(cart.final_total) }}</td>
            </tr>
          </tfoot>
        </table>
        <div class="input-group mb-3 input-group-sm">
          <input type="text" class="form-control" v-model="coupon_code" placeholder="請輸入優惠碼">
          <div class="input-group-append">
            <button class="btn btn-outline-secondary" type="button" @click="addCouponCode">
              套用優惠碼
            </button>
          </div>
        </div>
        <div class="text-right">
          <button class="btn btn-success" @click.prevent="rest">返回</button>
          <button class="btn btn-danger" @click.prevent="toCheckout">確認付款去</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cart: {},
      coupon_code: '',
    };
  },
  methods:{
    getOrder() {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/cart`;
      vm.isLoading = true;
      this.$http.get(api).then((response) => {
        vm.cart = response.data.data;
        console.log(response);
        vm.isLoading = false;
      });
    },
    removeCartItem(id) {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/cart/${id}`;
      vm.isLoading = true;
      this.$http.delete(api).then(() => {
        vm.getOrder();
        vm.isLoading = false;
        vm.$bus.$emit('message:push', '已刪除商品', 'success');
        vm.$bus.$emit('cart:updete');
      });
    },
    rest() {
      history.back();
    },
    toCheckout() {
      const vm = this;
      vm.$router.push(`/home/user_checkout`);
    },
    addCouponCode() {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/coupon`;
      const coupon = {
        code: vm.coupon_code
      };
      vm.isLoading = true;
      this.$http.post(api, {data: coupon }).then((response) => {
        if (response.data.success) {
          vm.getOrder();
          vm.$bus.$emit('cart:updete');
          vm.coupon_code = '';
          vm.isLoading = false;
        } else {
          this.$bus.$emit('message:push', response.data.message, 'danger');
          vm.$bus.$emit('cart:updete');
          vm.isLoading = false;
        };
      });
    },
  },
  created() {
    this.getOrder();
  },
};
</script>