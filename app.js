// 创建web服务
const express = require("express");
// 引入模块接收post数据
const bodyParser = require('body-parser');
// 创建后台页面路由
const adminRoutes = require("./routes/admin.js");
// 创建前台页面路由
const homeRoutes = require("./routes/home.js");

var app = express();
app.listen(8080);
app.use(express.static('public'));
app.use(bodyParser.urlencoded({
  extended:false  //不使用第三方的qs模块而是使用核心模块querystring来解析查询字符串
}));

app.use("/admin", adminRoutes);
app.use("", homeRoutes);


