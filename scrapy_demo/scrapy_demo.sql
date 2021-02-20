/*
Navicat MySQL Data Transfer

Source Server         : Local
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : test_db

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2021-02-20 11:09:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for scrapy_demo
-- ----------------------------
DROP TABLE IF EXISTS `scrapy_demo`;
CREATE TABLE `scrapy_demo` (
  `unique_key` varchar(64) NOT NULL COMMENT '唯一标识',
  `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
  `spider_time` datetime DEFAULT NULL COMMENT '爬取时间',
  `title` varchar(255) DEFAULT NULL COMMENT '标题',
  `city` varchar(255) DEFAULT NULL COMMENT '城市名',
  `area` varchar(255) DEFAULT NULL COMMENT '区域',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `product_type` varchar(64) DEFAULT NULL COMMENT '产品类型',
  `classified` varchar(64) DEFAULT NULL COMMENT '类别',
  `price` varchar(255) DEFAULT NULL COMMENT '价格',
  `source_site` varchar(255) DEFAULT NULL COMMENT '源网址',
  `version` int(11) DEFAULT '0' COMMENT '版本',
  `create_time` datetime DEFAULT NULL COMMENT '插入时间',
  `modify_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`unique_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
