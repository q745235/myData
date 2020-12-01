<template>
  <div>
    <loading :active.sync="isLoading"></loading>
    <div class="text-right mt-4">
      <button class="btn btn-primary" @click="openModal">建立新的優惠卷</button>
    </div>
    <table class="table mt-4">
      <thead>
        <tr>
          <th width="160">名稱</th>
          <th >折扣百分比</th>
          <th width="120">到期日</th>
          <th width="160">是否啟用</th>
          <th width="120">編輯</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item) in coupons" :key="item.id">
          <td>{{ item.title }}</td>
          <td>{{ item.percent }}%</td>
          <td class="text-right">{{ item.due_date | date }}</td>
          <td>
            <span v-if="item.is_enabled" class="text-success">啟用</span>
            <span v-else>未啟用</span>
          </td>
          <td>
            <button class="btn btn-outline-primary btn-sm" @click="openModal(false, item)">編輯</button>
            <button class="btn btn-outline-danger btn-sm" @click="deleteCoupon(item)">刪除</button>
          </td>
        </tr>
      </tbody>
    </table>
    <Pagination :pagination="pagination" @emitPage="getCoupons"></Pagination>

    <!-- Modal -->
    <div class="modal fade" id="couponModal" tabindex="-1" role="dialog"
      aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-md" role="document">
        <div class="modal-content border-0">
          <div class="modal-header bg-dark text-white">
            <h5 class="modal-title" id="exampleModalLabel">
              <span>新增產品</span>
            </h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col-sm-12">
                <div class="form-group">
                  <label for="title">標題</label>
                  <input type="text" class="form-control" id="title"
                    v-model="tempCoupon.title"
                    placeholder="請輸入標題">
                </div>
                <div class="form-group">
                  <label for="description">優惠碼</label>
                  <input type="text" class="form-control" id="coupon_code"
                    v-model="tempCoupon.code" 
                    placeholder="請輸入優惠碼">
                </div>
                <div class="form-group">
                  <label for="content">到期日</label>
                  <input type="date" class="form-control" id="due_date"
                    v-model="tempCoupon.due_date"
                    placeholder="請輸入到期日">
                </div>
                <div class="form-group">
                  <label for="origin_price">折扣百分比</label>
                    <input type="number" class="form-control" id="percent"
                      v-model="tempCoupon.percent"
                      placeholder="折扣百分比">
                  </div>
                <div class="form-group">
                  <div class="form-check">
                    <input class="form-check-input" type="checkbox"
                      v-model="tempCoupon.is_enabled"
                      :true-value="1"
                      :false-value="0"
                      id="is_enabled">
                    <label class="form-check-label" for="is_enabled">
                      是否啟用
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary" @click="updateCoupon">確認</button>
          </div>
        </div>
      </div>
    </div>

        <!-- CouponModal -->
    <div class="modal fade" id="delCouponModal" tabindex="-1" role="dialog"
      aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content border-0">
          <div class="modal-header bg-danger text-white">
            <h5 class="modal-title" id="exampleModalLabel">
              <span>刪除優惠卷</span>
            </h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            是否刪除 <strong class="text-danger">{{ tempCoupon.title }}</strong> 商品(刪除後將無法恢復)。
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-danger"
               @click="rellyDelet"
               >確認刪除</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import Pagination from '../Pagination';

export default {
  data() {
    return {
      coupons: {},
      pagination: {},
      tempCoupon: {},
      isLoading: false,
      isNew: false,
    };
  },
  components: {
    Pagination,
  },
  methods: {
    getCoupons(page = 1) {
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/admin/coupons?page=${page}`;
      const vm = this;
      vm.isLoading = true;
      this.$http.get(api).then((response) => {
        console.log(response.data);
        vm.isLoading = false;
        vm.coupons = response.data.coupons;
        vm.pagination = response.data.pagination;
      });
    },
    openModal(isNew, item) {
      if (isNew) {
        this.tempCoupon = {};
        this.isNew = true;
      } else {
        this.tempCoupon = Object.assign({}, item);
        const month =
          new Date(item.due_date * 1000).getMonth() < 9
            ? "0" + (new Date(item.due_date * 1000).getMonth() + 1)
            : new Date(item.due_date * 1000).getMonth() + 1;
        const date =
          new Date(item.due_date * 1000).getDate() < 10
            ? "0" + new Date(item.due_date * 1000).getDate()
            : new Date(item.due_date * 1000).getDate();
        this.tempCoupon.due_date = `${new Date(
          item.due_date * 1000
        ).getFullYear()}-${month}-${date}`;
        this.isNew = false;
      };
      $('#couponModal').modal('show');
    },
    updateCoupon() {
      let api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/admin/coupon`;
      let httpMethod = 'post';
      const vm = this;
      const timestamp = new Date(vm.tempCoupon.due_date).getTime();
      if (!vm.isNew) {
        api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/admin/coupon/${vm.tempCoupon.id}`;
        httpMethod = 'put';
      };
      vm.tempCoupon.due_date = Math.floor(timestamp / 1000); 
      this.$http[httpMethod](api, { data: vm.tempCoupon }).then((response) => {
        console.log(response.data);
        if (response.data.success) {
          $('#couponModal').modal('hide');
          vm.getCoupons();
          $('#delCouponModal').modal('hide');
        } else {
          $('#couponModal').modal('hide');
          vm.getCoupons();
          this.$bus.$emit('message:push', '新增失敗', 'danger');
          $('#delCouponModal').modal('hide');
        };
      });
    },
    deleteCoupon(item) {
      this.tempCoupon = item;
      $('#delCouponModal').modal('show');
    },
    rellyDelet() {
      const vm = this;
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/admin/coupons/${vm.tempCoupon.id}`;
      this.$http.delete(api, { data: vm.tempCoupon }).then((response) => {
        console.log(response.data);
        if (response.data.success) {
          vm.getCoupons();
          console.log('刪除成功');
          $('#delCouponModal').modal('hide');
        } else {
          vm.getCoupons();
          // console.log('刪除失敗');
           this.$bus.$emit('message:push', '刪除失敗', 'danger');
          $('#delCouponModal').modal('hide');
        };
      });
    },
  },
  created() {
    this.getCoupons();
  },
};
</script>