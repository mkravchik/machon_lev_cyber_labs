sudo apt-get update
#PHP is preinstalled
sudo apt-get install -y john python3 python-is-python3 gcc openssl mysql-server mysql-client php-cli php-mysql python3-pip wamerican-large python3-apt
#start mysql on boot
sudo update-rc.d mysql defaults
sudo update-rc.d mysql enable
#start it now
sudo service mysql start
#add 32 bit support
sudo dpkg --add-architecture i386
sudo apt-get install -y libc6-i386 libc6-dev-i386
sudo apt-get install -y gdb
sudo apt install python3-venv
python3 -m venv cyber
source cyber/bin/activate
pip3 install -r ./requirements.txt 

# create and populate the DB
# https://stackoverflow.com/questions/33991228/what-is-the-default-root-pasword-for-mysql-5-7/50305285#50305285 for details of password in new Ubuntu
set -e
sudo mysql -uroot <<MYSQL_SCRIPT
CREATE DATABASE IF NOT EXISTS users;
USE users;
create table if not exists t_users(user_id INT NOT NULL AUTO_INCREMENT,  first_name VARCHAR(100) NOT NULL, last_name  VARCHAR(100) NOT NULL, PRIMARY KEY(user_id));
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

# set the password hashing so that john 1.8 can work with it
sudo cp /etc/pam.d/common-password /etc/pam.d/common-password.bak
sudo sed -i '/pam_unix.so/ s/^.*$/password    [success=1 default=ignore]  pam_unix.so obscure sha512/' /etc/pam.d/common-password
if ! grep -q "pam_unix.so.*sha512" /etc/pam.d/common-password; then
  echo "Alert: The password hashing algorithm is not set to SHA-512."
fi
echo export PS1="$Uname:$">> ~/.bashrc

