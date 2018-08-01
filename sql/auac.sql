create database auac;
use auac;

CREATE TABLE user (
  id varchar(32) NOT NULL,
  username varchar(50) NOT NULL,
  password varchar(100) NOT NULL,
  realname varchar(50) DEFAULT NULL,
  mobile_number varchar(18) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO user VALUES('admin','admin','asdasdqwe1231dqwe123','小行星','1336336488');



select * from user;