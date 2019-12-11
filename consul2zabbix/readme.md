## Consul to Zabbix monitoring
### Consul or Zabbix? Use Both!  
With this template you can easily see Consul health checks on Zabbix.  
You can register a service on consul and see its status on Zabbix.  
It provides:
1. Auto-detection of Consul services.
2. Exposes Consul health check statuses to Zabbix.
3. Alerts if Consul health checks fail
4. Reports status of Consul node

## How to install
1. Make sure you have Python installed on the environment with your Zabbix Agent. This is important if you're running Zabbix inside of containers as Python will often not be included by default.
2. Create a scripts directory on the environment with your Zabbix Agent.
``` sudo mkdir /opt/scripts ```
3. Copy the script onto the server/container with your Zabbix Agent.
``` sudo cp consul2zabbix.py /opt/scripts/ ```
**Alternative:** If you do not wish to clone the entire repository onto this environment you can also use this command to get the script.
``` wget -P /opt/scripts/ https://raw.githubusercontent.com/dmitriy-myz/zabbix-templates/master/consul2zabbix/consul2zabbix.py ```
4. (Optional) If your Consul node is not in the same environment as your Agent then you will need to change consul address/port on line `19` to the address/port for your consul node.
5. Import the template consul2zabbix.xml to your Zabbix server. Change severity level. See [related docs](https://www.zabbix.com/documentation/current/manual/xml_export_import/templates) on how to do this.
6. Add Consul2Zabbix template to the Zabbix Hosts on which you want to map Consul services in Zabbix.
