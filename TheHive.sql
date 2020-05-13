DROP DATABASE IF EXISTS TheHive;
CREATE DATABASE TheHive;
use TheHive;

CREATE TABLE users(
    username VARCHAR(25),
    email VARCHAR(25),
    PRIMARY KEY(username, email),
    password VARCHAR(25),
    reputation_score INT DEFAULT 0,
    user_type ENUM('OU', 'VIP', 'SU'),
    status VARCHAR(5) NULL,
    votes INT DEFAULT 0,
    taboo_count INT DEFAULT 0
);

CREATE TABLE pending_users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    email VARCHAR(25) NOT NULL,
    reference VARCHAR(25) NOT NULL,
    interest VARCHAR(25) NOT NULL,
    credential VARCHAR(25) NOT NULL,
    UNIQUE KEY (email)
);

CREATE TABLE projects(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    description VARCHAR(50) NOT NULL,
    creator VARCHAR(25),
    projRank INT,
    viewing VARCHAR(5) DEFAULT NULL
);

CREATE TABLE group_membership(
    username VARCHAR(25),
    group_id INT,
    PRIMARY KEY(username, group_id),
    FOREIGN KEY(group_id) REFERENCES projects(id)
);

CREATE TABLE invitations(
    inviter VARCHAR(25),
    invited VARCHAR(25),
    group_id INT,
    FOREIGN KEY(inviter) REFERENCES users(username),
    FOREIGN KEY(invited) REFERENCES users(username),
    FOREIGN KEY(group_id) REFERENCES projects(id)
);

CREATE TABLE black_list(
    blacklister VARCHAR(25),
    blacklisted VARCHAR(25),
    PRIMARY KEY(blacklister, blacklisted),
    FOREIGN KEY(blacklister) REFERENCES users(username),
    FOREIGN KEY(blacklisted) REFERENCES users(username)
);

CREATE TABLE white_list(
    whitelister VARCHAR(25),
    whitelisted VARCHAR(25),
    PRIMARY KEY(whitelister, whitelisted),
    FOREIGN KEY(whitelister) REFERENCES users(username),
    FOREIGN KEY(whitelisted) REFERENCES users(username)
);

CREATE TABLE polls(
    entry VARCHAR(25),
    votes INT
);

CREATE TABLE posts(
    postid INT,
    group_id INT NOT NULL,
    username VARCHAR(25),
    content VARCHAR(225) NOT NULL,
    FOREIGN KEY(group_id) REFERENCES projects(id)
);
