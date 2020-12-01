<template>
  <div>
    <loading :active.sync="isLoading"></loading>
    <table class="table mt-4">
      <thead>
        <tr>
          <th width="180">購買時間</th>
          <th>Email</th>
          <th width="240">購買款項</th>
          <th width="120">應付金額</th>
          <th width="100">是否付款</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item) in orders" :key="item.id">
          <td>{{ item.create_at | date }}</td>
          <td>{{ item.user.email }}</td>
          <td>
            <ul>
              <li v-for="(product, i) in item.products" :key="i">
                {{ product.product.title }} 數量 : {{ product.qty }}
              </li>
            </ul>
          </td>
          <td class="text-right">
            {{ item.total | currency }}
          </td>
          <td>
            <span v-if="item.is_paid" class="text-success">已付款</span>
            <span v-else class="text-danger">還未繳清</span>
          </td>
        </tr>
      </tbody>
    </table>
    <Pagination :pagination="pagination" @emitPage="getOrders"></Pagination>
  </div>
</template>

<script>
import Pagination from '../Pagination';

export default {
  data() {
    return {
      orders: {},
      pagination: {},
      isLoading: false,
    };
  },
  components: {
    Pagination,
  },
  methods: {
    getOrders(page = 1) {
      const api = `${process.env.APIPATH}/api/${process.env.CUSTOMPATH}/admin/orders?page=${page}`;
      const vm = this;
      vm.isLoading = true;
      this.$http.get(api).then((response) => {
        console.log(response);
        vm.isLoading = false;
        vm.orders = response.data.orders;
        vm.pagination = response.data.pagination;
      });
    },
  },
  created() {
    this.getOrders();
  },
};
</script>