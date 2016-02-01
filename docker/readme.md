## Disc metrics


Provide: CPU usage, memory usage, process count, information about running containers.
Autodetect docker containers.
To calculate memory uses summ PSS memory of all running process in container


## How to install


``` bash
sudo mkdir /opt/scripts
sudo cp docker-count.sh /opt/scripts/
sudo cp docker-discover.py /opt/scripts/ 
sudo cp docker-stats.sh /opt/scripts/
sudo cp docker.conf /etc/zabbix/zabbix_agentd.conf.d/
```
add those lines to /etc/sudoers

```
zabbix ALL=(:docker) NOPASSWD:/usr/bin/docker ps -a --no-trunc
zabbix ALL=(root) NOPASSWD:/bin/cat /proc/*/smaps
```

Import template zbx_docker_templte.xml to zabbix server

