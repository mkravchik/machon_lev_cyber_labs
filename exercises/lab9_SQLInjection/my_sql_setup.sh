# I noticed that the no password login for the root user somehow disappeared from my DB
# This script restores is
# https://stackoverflow.com/questions/33991228/what-is-the-default-root-pasword-for-mysql-5-7/50305285#50305285 for details of password in new Ubuntu

set -e
sudo mysql --defaults-file=/etc/mysql/debian.cnf -uroot <<MYSQL_SCRIPT
USE mysql;
UPDATE user SET plugin='mysql_native_password' WHERE User='root';
COMMIT;
UPDATE mysql.user SET authentication_string=PASSWORD('') where user='root';
FLUSH PRIVILEGES;
COMMIT;
MYSQL_SCRIPT
sudo service mysql restart