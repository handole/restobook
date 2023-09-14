CREATE TABLE `users` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(250) NOT NULL,
    `fisrt_name` VARCHAR(250) NOT NULL,
    `last_name` VARCHAR(250) NOT NULL,
    `password_hash` VARCHAR(60) NOT NULL,
    `phone_number` VARCHAR(15),
    `is_superuser` BOOLEAN,
    `is_active` BOOLEAN,
    `created` DATETIME,
    `updated` DATETIME,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


CREATE TABLE `restaurants` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(250) NOT NULL,
    `address` VARCHAR(500),
    `is_active` BOOLEAN,
    `created` DATETIME,
    `updated` DATETIME,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


CREATE TABLE `tables` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `number` INT(20) NOT NULL,
    `resto_id` INT(20) NOT NULL,
    `is_active` BOOLEAN,
    `created` DATETIME,
    `updated` DATETIME,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


CREATE TABLE `menu` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(250) NOT NULL,
    `price` DECIMAL,
    `is_active` BOOLEAN,
    `stock` INT,
    `created` DATETIME,
    `updated` DATETIME,
    `resto_id` INT(20) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


CREATE TABLE `reservation` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `user_id` INT(20) NOT NULL,
    `created` DATETIME,
    `updated` DATETIME,
    `is_active` BOOLEAN,
    `table_id` INT(20),
    `menu_id` INT(20),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


CREATE TABLE `tickets` (
    `id` INT(20) NOT NULL AUTO_INCREMENT,
    `user_id` INT(20) NOT NULL,
    `created` DATETIME,
    `updated` DATETIME,
    `price` INT(20),
    `is_active` BOOLEAN,
    `table_id` INT(20),
    `menu_id` INT(20),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;