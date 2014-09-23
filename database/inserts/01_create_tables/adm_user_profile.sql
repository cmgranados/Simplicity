
REATE TABLE `adm_user_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `registration_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `adm_user_profile_1f3b2608` (`registration_type_id`),
  CONSTRAINT `registration_type_id_refs_type_id_7ee61079` FOREIGN KEY (`registration_type_id`) REFERENCES `adm_type` (`type_id`),
  CONSTRAINT `user_id_refs_id_2e40a2c4` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
)