
## Apache auf raspberrypi3
Vorbereitung (update + upgrade dauert ca. 10 min):
```bash
sudo apt-get update && sudo apt-get upgrade
```
### Apache

```bash
sudo apt-get install apache2 -y
```
Check with http://raspberrpi3 or http://192.168.5.47

### Set permissions on the web directory /var/www/
It is useful to change the permissions on the www directory to allow your user to update the webpages without needing to be root.

```bash
#Change the directory owner and group
sudo chown -R www-data:www-data /var/www

#allow the group to write to the directory
sudo chmod -R 775 /var/www

#Add the pi user to the www-data group
sudo usermod -a -G www-data pi
```
You must logout and back in - to pick up the new group permissions, or if running X you can just start a new terminal.
