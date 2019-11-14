import textfsm
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result
from pprint import pprint




"""
nr = InitNornir()
print(nr.inventory.hosts)



result = nr.run(napalm_get, getters=['get_interfaces_counters'])

print(result['rtr1'][0].result['get_interfaces_counters']['Ethernet0/0']['rx_octets'])

for device in result.items():
    for interface in device[1].result['get_interfaces_counters'].items():
     if interface[1]['rx_octets'] :
         print("{} {} rx octets: {}".format(device[0], interface[0], interface[1]['rx_octets']))

result = nr.run(napalm_get, getters=['get_route_to'], getters_options={"get_route_to" : {'destination' : '192.168.10.12'}})
print(result['rtr1'][0].result['get_route_to'])

result = nr.run(task=netmiko_send_command, command_string="show version")
pprint(result['rtr1'][0].result)
"""
version = """
Cisco IOS Software, Linux Software (I86BI_LINUX-ADVENTERPRISEK9-M), Version 15.5(2)T, DEVELOPMENT TEST SOFTWARE
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Thu 26-Mar-15 07:36 by prod_rel_team

ROM: Bootstrap program is Linux

R1 uptime is 8 hours, 5 minutes
System returned to ROM by reload at 0
System image file is "unix:/opt/unetlab/addons/iol/bin/i86bi-linux-l3-adventerprisek9-15.5"
Last reload reason: Unknown reason



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Linux Unix (Intel-x86) processor with 87588K bytes of memory.
Processor board ID 67108880
16 Ethernet interfaces
1024K bytes of NVRAM.



Configuration register is 0x0

"""

with open('cisco_ios_show_version.template', 'r') as f:
    template = textfsm.TextFSM(f)
    next_hop = template.ParseText(version)
print(next_hop)

route = """
Routing entry for 172.16.30.4/31
  Known via "eigrp 90", distance 90, metric 332800, type internal
  Redistributing via eigrp 90
  Last update from 10.10.10.0 on Ethernet2/0, 00:00:11 ago
  Routing Descriptor Blocks:
  * 192.168.10.12, from 192.168.10.12, 00:00:11 ago, via Ethernet0/2
      Route metric is 332800, traffic share count is 1
      Total delay is 3000 microseconds, minimum bandwidth is 10000 Kbit
      Reliability 255/255, minimum MTU 1500 bytes
      Loading 1/255, Hops 2
    10.10.10.0, from 10.10.10.0, 00:00:11 ago, via Ethernet2/0
      Route metric is 332800, traffic share count is 1
      Total delay is 3000 microseconds, minimum bandwidth is 10000 Kbit
      Reliability 255/255, minimum MTU 1500 bytes
      Loading 1/255, Hops 2

"""

with open('show_ip_route_destination.template', 'r') as f:
    template = textfsm.TextFSM(f)
    next_hop = template.ParseText(route)
print(next_hop)
for i in next_hop:
    print(i[2])


#print_result(result)
#print(result['rtr1'][0].result[0]['interface'],result['rtr1'][0].result[0]['output_rate'])