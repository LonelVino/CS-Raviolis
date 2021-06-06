webpackJsonp([12],{"Ekv/":function(e,t){},NspC:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=r("woOf"),o=r.n(n),a=r("Xxa5"),i=r.n(a),l=r("exGp"),s=r.n(l),c=r("S49b"),d=r("vLgD"),u="/api_v1/order";var _=r("1onU"),f=r("cAgV"),p={name:"OrderTable",components:{Pagination:_.a},directives:{waves:f.a},data:function(){return{listLoading:!1,tableKey:0,usr_id:13,order_items:null,orders:null,all_order_items:[],tmp_prod_info:null,idx:0,dialogFormVisible:!1,dialogStatus:"",confirmLoading:!1}},created:function(){this.getList()},computed:{noOrder:function(){return null==this.orders}},methods:{getList:function(){var e=this;return s()(i.a.mark(function t(){var r,n;return i.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return e.listLoading=!0,t.next=3,a=e.usr_id,Object(d.a)({url:u+"/usr_all_ords?usr_id="+a,method:"get"});case 3:for(r=t.sent,e.orders=r.data.order_infos,n=0;n<e.orders.length;n++)e.orders[n].paid=1==e.orders[n].paid||1==e.orders[n].paid?1:0;for(n=0;n<e.orders.length;n++)(o=e.orders[n].id,Object(d.a)({url:u+"/usr_ord_itms?id="+o,method:"get"})).then(function(t){e.all_order_items.push(t.data.order_items_info),e.getProdbyId(e.idx).then(e.idx++),setTimeout(function(){e.listLoading=!1},1500)}).catch(function(e){console.error(e)});console.log("ORDERS:",e.orders),console.log("ALL ORDER ITEMS:",e.all_order_items);case 9:case"end":return t.stop()}var o,a},t,e)}))()},getProdbyId:function(e){var t=this;return s()(i.a.mark(function r(){var n,a;return i.a.wrap(function(r){for(;;)switch(r.prev=r.next){case 0:t.all_order_items[e].prod_name="",t.all_order_items[e].dt_info="",t.all_order_items[e].mini_num="",n=0;case 4:if(!(n<t.all_order_items[e].length)){r.next=16;break}return r.next=7,Object(c.d)(t.all_order_items[e][n].product_id);case 7:a=r.sent,t.tmp_prod_info=a.data.prod_info,o()(t.all_order_items[e][n],{prod_name:t.tmp_prod_info.name,dt_info:t.tmp_prod_info.dt_info,mini_num:t.tmp_prod_info.quantity_unit}),t.all_order_items[e][n].gotten=1==t.all_order_items[e][n].gotten||1==t.all_order_items[e][n].gotten?1:0,t.$set(t.all_order_items[e][n],"ttl_price",t.all_order_items[e][n].itm_price*t.all_order_items[e][n].quantity),t.orders[e].usr_price+=t.all_order_items[e][n].itm_price*t.all_order_items[e][n].quantity;case 13:n++,r.next=4;break;case 16:o()(t.orders[e],{order_items:t.all_order_items[e]}),t.orders[e].created=t.orders[e].created.substr(5,5);case 18:case"end":return r.stop()}},r,t)}))()},handleChangeGotten:function(e){var t,r=this,n={id:e.id,gotten:e.gotten};(t=n,Object(d.a)({url:u+"/check_usr_one_itm",method:"put",data:t})).then(function(t){var n=0==e.gotten?"False":"True";r.$notify({title:"Success",message:"Status Changed into "+n.toUpperCase(),type:"success",duration:2e3})})},handleChangeOrderPaid:function(e,t){var r,n=this;(r={ord_id:e,paid:t},Object(d.a)({url:u+"/check_ord_paid",method:"put",data:r})).then(function(e){var r=0==t?"False":"True";n.$notify({title:"Success",message:"Payment Status Changed into "+r.toUpperCase(),type:"success",duration:2e3})}).catch(function(e){console.error(e)})},confirmDeleteItem:function(e){var t=this;this.$confirm("This operation will delete this item forever, are you sure?","Note",{confirmButtonText:"Confirm",cancelButtonText:"Cancle",type:"warning"}).then(function(){t.handleDeleteItem(e)}).catch(function(){t.$message({type:"info",message:"Delete cancled"})})},handleDeleteItem:function(e){var t,r=this;console.log("INDEX:",e),(t=e,Object(d.a)({url:u+"/delete_usr_one_itm?id="+t,method:"delete"})).then(function(){r.$notify({title:"Success",message:"Delete Successfully",type:"success",duration:2e3}),r.refreshTable()}).catch(function(e){r.$notify({title:"Failed",message:"Delete failed",type:"danger",duration:2e3})})},confirmDeleteOrder:function(e){var t=this;this.$confirm("This operation will delete this order forever, are you sure?","Note",{confirmButtonText:"Confirm",cancelButtonText:"Cancle",type:"warning"}).then(function(){t.handleDeleteOrder(e)}).catch(function(){t.$message({type:"info",message:"Delete cancled"})})},handleDeleteOrder:function(e){var t,r=this;console.log("INDEX:",e),(t=e,Object(d.a)({url:u+"/delete_usr_ord?id="+t,method:"delete"})).then(function(){r.$notify({title:"Success",message:"Delete Successfully",type:"success",duration:2e3}),r.refreshTable()}).catch(function(e){r.$notify({title:"Failed",message:"Delete failed",type:"danger",duration:2e3})})},refreshTable:function(){this.idx=0,this.getList()}}},m={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"app-container"},[e.noOrder?r("div",{staticClass:"notify"},[e._v("\n    None\n  ")]):e._e(),e._v(" "),e._l(e.orders,function(t){return r("div",{staticClass:"orders"},[r("div",{staticClass:"user-order"},[r("el-row",{attrs:{gutter:12}},[r("el-col",{attrs:{span:3.5}},[r("el-card",{staticClass:"first-card",attrs:{shadow:"hover"}},[r("span",{staticClass:"first-card-txt"},[e._v(e._s(t.created)+" ORDER")])])],1),e._v(" "),r("el-col",{attrs:{span:6}},[r("el-card",{staticClass:"second-card",attrs:{shadow:"hover"}},[r("span",[e._v("Total Price:  "+e._s(t.usr_price)+" €")])])],1),e._v(" "),r("el-col",{attrs:{span:6}},[r("el-card",{staticClass:"second-card",attrs:{shadow:"hover"}},[r("span",[e._v("Has paid:")]),e._v(" "),r("el-switch",{attrs:{"active-value":1,"inactive-value":0,"active-color":"#02538C","inactive-color":"#B9B9B9"},on:{change:function(r){return e.handleChangeOrderPaid(t.id,t.paid)}},model:{value:t.paid,callback:function(r){e.$set(t,"paid",r)},expression:"order.paid"}})],1)],1),e._v(" "),r("el-col",{attrs:{span:3}},[r("div",{staticClass:"remove-all"},[r("el-button",{staticStyle:{height:"3vw","margin-top":"-1vw","font-size":"1vw","font-weight":"bolder",color:"#a04949"},attrs:{type:"warning"},on:{click:function(r){return e.confirmDeleteOrder(t.id)}}},[e._v("\n              Remove Order\n            ")])],1)])],1)],1),e._v(" "),r("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.listLoading,expression:"listLoading"}],key:e.tableKey,ref:"multipleTable",refInFor:!0,staticClass:"order-table",staticStyle:{width:"100%"},attrs:{data:t.order_items,border:"",fit:"","highlight-current-row":""}},[r("el-table-column",{attrs:{prop:"id",label:"ID",width:"50px",align:"center","show-overflow-tooltip":""}}),e._v(" "),r("el-table-column",{attrs:{label:"Product",width:"200px",align:"center","show-overflow-tooltip":""},scopedSlots:e._u([{key:"default",fn:function(t){return[r("div",[e._v(" "+e._s(t.row.prod_name))])]}}],null,!0)}),e._v(" "),r("el-table-column",{attrs:{prop:"mini_num",label:"Num(/1 Unit)",width:"150px",align:"center","show-overflow-tooltip":""}}),e._v(" "),r("el-table-column",{attrs:{label:"Unit Price",align:"center","show-overflow-tooltip":""},scopedSlots:e._u([{key:"default",fn:function(t){return[r("div",[e._v(" "+e._s(t.row.itm_price)+" €")])]}}],null,!0)}),e._v(" "),r("el-table-column",{attrs:{prop:"quantity",label:"Quantity",align:"center","show-overflow-tooltip":""}}),e._v(" "),r("el-table-column",{attrs:{prop:"ttl_price",label:"Total",align:"center","show-overflow-tooltip":""},scopedSlots:e._u([{key:"default",fn:function(t){return[r("div",[e._v(" "+e._s(t.row.ttl_price)+" €")])]}}],null,!0)}),e._v(" "),r("el-table-column",{attrs:{label:"Has Gotten",width:"100px",align:"center","show-overflow-tooltip":""},scopedSlots:e._u([{key:"default",fn:function(t){return[r("el-switch",{attrs:{"active-value":1,"inactive-value":0,"active-color":"#02538C","inactive-color":"#B9B9B9"},on:{change:function(r){return e.handleChangeGotten(t.row)}},model:{value:t.row.gotten,callback:function(r){e.$set(t.row,"gotten",r)},expression:"scope.row.gotten"}})]}}],null,!0)}),e._v(" "),r("el-table-column",{attrs:{label:"Actions",align:"center","class-name":"small-padding fixed-width"},scopedSlots:e._u([{key:"default",fn:function(t){var n=t.row;return["deleted"!=n.status?r("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(t){return e.confirmDeleteItem(n.id)}}},[e._v("\n            Remove\n          ")]):e._e()]}}],null,!0)})],1)],1)})],2)},staticRenderFns:[]};var h=r("VU/8")(p,m,!1,function(e){r("iAxx"),r("Ekv/")},"data-v-6bd7c6d6",null);t.default=h.exports},iAxx:function(e,t){}});
//# sourceMappingURL=12.1ae5c8ea89e07a6e8751.js.map