## Disc metrics


Provides disk usage: iops count, disk space usage, triggers.


##TODO 
 software raid information


## How to install


``` bash

sudo mkdir /opt/scripts
sudo cp diskstats.sh /opt/scripts/
sudo cp diskstat.conf /etc/zabbix/zabbix_agentd.conf.d/
```

Import template zbx_linux_disk_metrics.xml

