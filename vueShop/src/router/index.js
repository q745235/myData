import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import Dashboard from '@/components/Dashboard'
import Login from '@/components/pages/Login'
import Products from '@/components/pages/Products'
import Coupons from '@/components/pages/Coupons'
import Orders from '@/components/pages/Orders'
import CustomerOrder from '@/components/pages/CustomerOrders'
import CustomerCheckout from '@/components/pages/CustomerCheckout'

//Front
import Home from '@/components/Front/Home'
import ProductDetail from '@/components/Front/pages/ProductDetail'
import CustomerProducts from '@/components/Front/pages/CustomerProducts'
import UserOrder from '@/components/Front/pages/UserOrder'
import UserCheckout from '@/components/Front/pages/UserCheckout'
import UserPay from '@/components/Front/pages/UserPay'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '*',
      redirect: 'home/customer_products/全部',
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      children: [
        {
          path: 'customer_products/:category',
          name: 'CustomerProducts',
          component: CustomerProducts,
        },
        {
          path: 'product_detail/:productId',
          name: 'ProductDetail',
          component: ProductDetail,
        },
        {
          path: 'orders',
          name: 'Orders',
          component: Orders,
        },
        {
          path: 'coupons',
          name: 'Coupons',
          component: Coupons,
        },
        {
          path: 'user_order',
          name: 'UserOrder',
          component: UserOrder,
        },
        {
          path: 'user_pay/:orderId',
          name: 'UserPay',
          component: UserPay,
        },
        {
          path: 'user_checkout',
          name: 'UserCheckout',
          component: UserCheckout,
        },
      ],
    },
    
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld,
    //   meta: { requiresAuth: true },
    // },

    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    
    {
      path: '/admin',
      name: 'Dashboard',
      component: Dashboard,
      children: [
        {
          path: 'products',
          name: 'Products',
          component: Products,
          meta: { requiresAuth: true },
        },
        {
          path: 'orders',
          name: 'Orders',
          component: Orders,
          meta: { requiresAuth: true },
        },
        {
          path: 'coupons',
          name: 'Coupons',
          component: Coupons,
          meta: { requiresAuth: true },
        },
      ],
    },

    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard,
      children: [
        {
          path: 'customer_order',
          name: 'CustomerOrder',
          component: CustomerOrder,
        },
        {
          path: 'customer_checkout/:orderId',
          name: 'CustomerCheckout',
          component: CustomerCheckout,
        },
      ],
    },
  ],
});
