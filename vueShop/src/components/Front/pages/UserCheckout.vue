<template>
  <div>
    <loading :active.sync="isLoading"></loading>
    <div class="my-5 row justify-content-center">
      <form class="col-md-6" @submit.prevent="createdOrder">
        <div class="form-group">
          <label for="useremail">Email</label>
          <input type="email" class="form-control" name="email" id="useremail"
            v-validate="'required|email'"
            v-model="form.user.email" placeholder="請輸入 Email">
          <span class="text-danger" v-if="errors.has('email')">
            {{ errors.first('email') }}
          </span>
        </div>
      
        <div class="form-group">
          <label for="username">收件人姓名</label>
          <input type="text" class="form-control" name="name" id="username"
            :class="{'is-invalid': errors.has('name')}"
            v-model="form.user.name" v-validate="'required'" placeholder="輸入姓名">
          <span class="text-danger" v-if="errors.has('name')">姓名必需輸入</span>
        </div>
      
        <div class="form-group">
          <label for="usertel">收件人電話</label>
          <input type="tel" name="tel" class="form-control" id="usertel" v-model="form.user.tel"
           v-validate="'required|digits:10'" placeholder="請輸入電話">
           <span class="text-danger" v-if="errors.has('tel')">
            {{ errors.first('tel').replace(/tel/, '電話') }}
          </span>
        </div>
      
        <div class="form-group">
          <label for="useraddress">收件人地址</label>
          <input type="text" class="form-control" name="address" id="useraddress" v-model="form.user.address"
           v-validate="'required'" placeholder="請輸入地址">
          <span class="text-danger" v-if="errors.has('address')">地址欄位不得留空</span>
        </div>
      
        <div class="form-group">
          <label for="comment">留言</label>
          <textarea name="" id="comment" class="form-control" cols="30" rows="10" v-model="form.message"></textarea>
        </div>
        <div class="text-right">
          <button class="btn btn-danger">送出訂單</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoading: false,
      form: {
        user: {
          name: '',
          email: '',
          tel: '',
          address: '',
        },
        message: '',
      },
      orderId: '',
    };
  },
  methods: {
    rest() {
      history.back();
    },
    createdOrder() {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/order`;
      const order = vm.form;
      // vm.isLoading = true;
      this.$validator.validate().then((valid) => {
        if (valid) {
          this.$http.post(api, {data: order}).then((response) => {
          console.log('訂單已建立', response);
          if (response.data.success) {
            vm.$router.push(`/home/user_pay/${response.data.orderId}`);
          }
          vm.isLoading = false;
          });
        } else {
          console.log('欄位不完整');
          vm.isLoading = false;
        };
      });
    },
  },
};
</script>