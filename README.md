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


##4) Third party sources
No third party sources were used outside of the Udacity forums and the sources provided by Udacity itself. 
