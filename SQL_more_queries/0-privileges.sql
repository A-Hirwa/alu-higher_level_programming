-- Lists all privileges of the users user_0d_1 and user_0d_2.
SELECT 'Privileges for user_0d_1@localhost' AS User_Info;
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SELECT 'Privileges for user_0d_2@localhost' AS User_Info;
SHOW GRANTS FOR 'user_0d_2'@'localhost';
