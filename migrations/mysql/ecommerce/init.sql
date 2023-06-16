CREATE TABLE `products` (
    `id`       int NOT NULL AUTO_INCREMENT,
    `name`     varchar(36) NOT NULL,
    `price`    decimal(12,2) NOT NULL,
    `category` varchar(36) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
