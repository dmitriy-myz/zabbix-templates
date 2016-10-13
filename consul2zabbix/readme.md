## consul2zabbix mapper


Provide: consul health check status to zabbix.
Autodetect consul services.



## How to install


``` bash
sudo mkdir /opt/scripts
sudo cp consul2zabbix.py /opt/scripts/
```
change consul address/port to actual value
Import template consul2zabbix.xml to zabbix server. Change severity level.

Add Consul2Zabbix template to nodes.

