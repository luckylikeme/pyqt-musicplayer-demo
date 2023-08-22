/*
 Navicat Premium Data Transfer

 Source Server         : database_host
 Source Server Type    : MySQL
 Source Server Version : 80034
 Source Host           : localhost:3306
 Source Schema         : music_player

 Target Server Type    : MySQL
 Target Server Version : 80034
 File Encoding         : 65001

 Date: 22/08/2023 14:55:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for song_detail
-- ----------------------------
DROP TABLE IF EXISTS `song_detail`;
CREATE TABLE `song_detail`  (
  `song_id` int NOT NULL,
  `song_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `singer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `song_words` varchar(600) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `detail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`song_id`) USING BTREE,
  CONSTRAINT `fk_3` FOREIGN KEY (`song_id`) REFERENCES `songs` (`song_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of song_detail
-- ----------------------------
INSERT INTO `song_detail` VALUES (1, '想你时风起', '单依纯', '\"D:\\songs\\text\\想你时风起.txt\"', '《人间烟火》主题曲');

-- ----------------------------
-- Table structure for song_list
-- ----------------------------
DROP TABLE IF EXISTS `song_list`;
CREATE TABLE `song_list`  (
  `user_id` int NOT NULL,
  `song_id` int NOT NULL,
  PRIMARY KEY (`user_id`, `song_id`) USING BTREE,
  INDEX `fk_5`(`song_id`) USING BTREE,
  CONSTRAINT `fk_4` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_5` FOREIGN KEY (`song_id`) REFERENCES `songs` (`song_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of song_list
-- ----------------------------

-- ----------------------------
-- Table structure for songs
-- ----------------------------
DROP TABLE IF EXISTS `songs`;
CREATE TABLE `songs`  (
  `song_id` int NOT NULL AUTO_INCREMENT,
  `file_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`song_id`) USING BTREE,
  UNIQUE INDEX `file_url`(`file_url`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of songs
-- ----------------------------
INSERT INTO `songs` VALUES (1, '\"D:\\songs\\想你时风起.mp3\"');

-- ----------------------------
-- Table structure for user_like
-- ----------------------------
DROP TABLE IF EXISTS `user_like`;
CREATE TABLE `user_like`  (
  `user_id` int NOT NULL,
  `song_id` int NOT NULL,
  PRIMARY KEY (`user_id`, `song_id`) USING BTREE,
  INDEX `fk_2`(`song_id`) USING BTREE,
  CONSTRAINT `fk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_2` FOREIGN KEY (`song_id`) REFERENCES `songs` (`song_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_like
-- ----------------------------

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nick_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `sex` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `auth` int NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'user_test', 'user1', '男', '123456', 0);

SET FOREIGN_KEY_CHECKS = 1;
