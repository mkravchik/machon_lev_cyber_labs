sudo apt-get update
#PHP is preinstalled
sudo apt-get install john python gcc openssl mysql-server mysql-client apache2 subversion python-pip python-crypto wamerican-large python-apt
#start mysql on boot
sudo update-rc.d mysql defaults
sudo update-rc.d mysql enable
#start it now
sudo service mysql start
#add 32 bit support
sudo dpkg --add-architecture i386
sudo apt-get install libc6-i386 libc6-dev-i386

pip install -r ./requirements.txt
# create and populate the DB - ALREADY PRESENT in the image
# https://stackoverflow.com/questions/33991228/what-is-the-default-root-pasword-for-mysql-5-7/50305285#50305285 for details of password in new Ubuntu
# Can login using sudo mysql --defaults-file=/etc/mysql/debian.cnf
# set -e
# mysql -uroot <<MYSQL_SCRIPT
# CREATE DATABASE IF NOT EXISTS users;
# USE users;
# create table t_users(user_id INT NOT NULL AUTO_INCREMENT,  first_name VARCHAR(100) NOT NULL, last_name  VARCHAR(100) NOT NULL, PRIMARY KEY(user_id));
# insert into t_users (first_name, last_name) VALUES ("Alice", "Wonderland");
# insert into t_users (first_name, last_name) VALUES ("Bob", "Sponge");
# insert into t_users (first_name, last_name) VALUES ("Jim", "Naive-Admin");
# MYSQL_SCRIPT
