sudo apt-get update
#PHP is preinstalled
sudo apt-get install -y john python3 gcc openssl mysql-server mysql-client apache2 subversion python3-pip wamerican-large python3-apt
#start mysql on boot
sudo update-rc.d mysql defaults
sudo update-rc.d mysql enable
#start it now
sudo service mysql start
#add 32 bit support
sudo dpkg --add-architecture i386
sudo apt-get install -y libc6-i386 libc6-dev-i386
sudo apt-get install -y gdb

pip install -r ./requirements.txt
# create and populate the DB
# https://stackoverflow.com/questions/33991228/what-is-the-default-root-pasword-for-mysql-5-7/50305285#50305285 for details of password in new Ubuntu
set -e
sudo mysql --defaults-file=/etc/mysql/debian.cnf -uroot <<MYSQL_SCRIPT
CREATE DATABASE IF NOT EXISTS users;
USE users;
create table t_users(user_id INT NOT NULL AUTO_INCREMENT,  first_name VARCHAR(100) NOT NULL, last_name  VARCHAR(100) NOT NULL, PRIMARY KEY(user_id));
insert into t_users (first_name, last_name) VALUES ("Alice", "Wonderland");
insert into t_users (first_name, last_name) VALUES ("Bob", "Sponge");
insert into t_users (first_name, last_name) VALUES ("Jim", "Naive-Admin");
USE mysql;
UPDATE user SET plugin='mysql_native_password' WHERE User='root';
ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY '';
FLUSH PRIVILEGES;
MYSQL_SCRIPT
sudo service mysql restart

echo "enter your username in JCT"
read Uname
cp ~/.bashrc ~/.bashrc.bak
sed -i s/\$C9_USER/$Uname/g ~/.bashrc
