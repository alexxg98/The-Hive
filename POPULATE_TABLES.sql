INSERT INTO
users(email, username, password, user_type)
VALUES
("niharika@gmail.com", "nalam001", "123", "SU"),
("michael@gmail.com", "michael002", "123", "SU"),
("alex@gmail.com", "alex003", "123", "SU"),
("linda@gmail.com", "linda004", "123", "SU");
UPDATE users SET status = 'ON' where username = 'alex003';

INSERT INTO
users(email, username, password, reputation_score, user_type)
VALUES
("fox@gmail.com", "mfox456", "123", 10, "OU"),
("sun@gmail.com", "msun246", "123", 15, "OU"), 
("moon@gmail.com", "lmoon541py ", "123", 24, "OU"),
("star@gmail.com", "vstar216", "123", 35, "VIP"),
("sky@gmail.com", "ssky753", "123", 37, "VIP");

INSERT INTO
pending_users(name, email, reference, interest, credential)
VALUES
("Nicky Minaj", "nicki@gmail.com", "reference", "interest", "credential"),
("Aster Fallon", "aster@gmail.com", "reference", "interest", "credential"),
("Adele", "adele@gmail.com", "reference", "interest", "credential"),
("Romeo", "romeo@gmail.com", "reference", "interest", "credential");

INSERT into
projects(id, name, description, creator, projRank)
VALUES
(1, "Group1", "Sample Group/Project #1", "ssky753", 1),
(2, "Group2", "Sample Group/Project #2", "lmoon541", 2),
(3, "Group3", "Sample Group/Project #3", "mfox456", 3),
(4, "Group4", "Sample Group/Project #4", "vstar216", 4);

INSERT into 
group_membership(username, group_id) 
VALUES 
("ssky753", 1),
("lmoon541", 2),
("mfox456", 3),
("vstar216", 3),
("msun246", 2),
("msun246", 1);

INSERT into
posts(postid, group_id, username, content)
VALUES
(1, 1, "ssky753", "Hello. Welcome to the group #1!"),
(1, 2, "lmoon541", "Hello. Welcome to the group #2!"),
(1, 3, "mfox456", "Hello. Welcome to the group #3!"),
(1, 4, "vstar216", "Hello. Welcome to the group #4!");

