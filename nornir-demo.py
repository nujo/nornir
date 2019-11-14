import textfsm
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result
from pprint import pprint





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

