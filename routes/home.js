const express = require('express');
const pool = require('../pool.js');
// 创建路由器
var router = express.Router();

router.get("/", function (req,res) {
  var dirname = __dirname.slice(0, -7);
  res.sendFile(dirname + "/public/home/home.html");
});

router.get("/login", function (req, res) {
  var dirname = __dirname.slice(0, -7);
  res.sendFile(dirname + "/public/home/login.html");
});

router.get("/register", function (req, res) {
  var dirname = __dirname.slice(0, -7);
  res.sendFile(dirname + "/public/home/register.html");
});

router.get("/user", function (req, res) {
  var dirname = __dirname.slice(0, -7);
  res.sendFile(dirname + "/public/home/user.html");
});
// 导出路由
module.exports = router;


