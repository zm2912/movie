const express = require('express');
const pool = require('../pool.js');
// 创建路由器
var router = express.Router();

router.get("/index", (req,res) => {
  res.send("后台主页");
});


// 导出路由对象
module.exports = router;