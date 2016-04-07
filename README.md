# Linux web server and catalog app
----------------

##1) IP address and SSH port
IP: 52.10.151.247  
SSH port: 2200

##2) URL of hosted web page
http://ec2-52-10-151-247.us-west-2.compute.amazonaws.com

##3) Summary of software installed and configurations made
### Updated all packages
$sudo apt-get update
$sudo apt-get upgrade
### Allow packages to auto-update
$sudo apt-get install -y unattended-upgrades  
$sudo dpkg-reconfigure -plow unattended-upgrades
### Configured timezone to UTC
$sudo dpkg-reconfigure tzdat  
Followed prompt: select none of the above, then UTC
###Setup ufw
$ufw status #should say inactive  
$sudo ufw default deny incoming  
$sudo ufw default allow outgoing  
$sudo ufw allow 123/udp  
$sudo ufw allow 2200/tcp  
$sudo ufw allow 80/tcp  
$sudo ufw enable  

### Installed ntp for clock sync
$apt-get install -y ntp

### Installed apache
$sudo apt-get install apache2

### Installed mod_msgi
$sudo apt-get install libapache2-mod-wsgi

### Updated /etc/apache2/sites-enabled/000-default.conf
$sudo nano /etc/apache2/sites-enabled/000-default.conf  
Added the following line at the end of the <VirtualHost *:80> block right before the closing </VirtualHost> line:  
WSGIScriptAlias / /var/www/html/myapp.wsgi

### Create /var/www/html/myapp.wsgi
$sudo nano /var/www/html/myapp.wsgi

### Wrote application within myapp.wsgi to add site app to python's PATH so imports can be used
import sys  
sys.path.insert(0, '/home/grader/PV-Catalog-PSQL')  
from myapp import app as application

### Installed postgresql
$sudo apt-get install postgresql

### Confirmed remote connection to db not allowed (already set by default)
$sudo nano /etc/postgresql/9.3/main/pg_hba.conf

### Created new role 'catalog'
$sudo su - postgres  
$psql  
$CREATE ROLE catalog WITH createdb;
### Created pvequipment.db and gave ownership to 'catalog'
$CREATE DATABASE pvequipment WITH OWNER catalog;

### Installed git
sudo apt-get install git-all

### Cloned repository
git clone https://github.com/mepurser/PV-Catalog-PSQL

### Installed pip, then using pip, flask, oauth2client, sqlalchemy
sudo apt-get install python-pip
sudo pip install Flask
sudo pip install --upgrade oauth2client
sudo pip install SQLAlchemy

##4) Third party sources
No third party sources were used outside of the Udacity forums and the sources provided by Udacity itself. 
