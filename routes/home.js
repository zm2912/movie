const express = require('express');
const pool = require('../pool.js');
// 创建路由器
var router = express.Router();

router.get("/", (req,res) => {
  res.send("前台主页");
});

// 导出路由
module.exports = router;


