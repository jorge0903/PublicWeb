# Public Facing Web

This program will have to be in: 

Location for files: /var/www/html/

Permissions: 766

## Configure

Configure your home router so that it translates requests over an specific port to your localhost using your public ip

### Example:

If ip is: 169.12.34.53 and you have configured your local host to listen on port 8080, then you can access your server as: http://169.12.34.53

On your router you shold configure something as follows and assuming your localhost ip is 192.168.0.34: 
 * Firewall/NAT_or_Gamming
 * Select your Service as HTTP or HTTPS
 * Select your Ports, in this case: tcp 8080 
 * Select your Device's ip, in this case: 192.168.0.34


When done, your table should look something similar as:

... > Firewall > NAT_or_Gamming

----------------------------------
| Service | Ports | Device       |
|---------|-------|--------------| 
| HTTP    | 8080  | 192.168.0.34 |
|  ...    |  ...  |    ...       |
| HTTPS   | 8080  | 192.168.0.34 |
---------------------------------- 
