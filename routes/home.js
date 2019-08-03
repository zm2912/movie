const express = require('express');
const pool = require('../pool.js');
// 创建路由器
var router = express.Router();

router.get("/", function (req,res) {
  var dirname = __dirname.slice(0, -7);
  res.sendFile(dirname + "/public/home/index.html");
});

// 导出路由
module.exports = router;


