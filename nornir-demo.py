import textfsm
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result
from pprint import pprint
from nornir.plugins.tasks.networking import netmiko_file_transfer






# let's pretend we used raw_input or something like that
password = input("Please, enter password: ")

nr = InitNornir()
nr.inventory.defaults.password = password
print(nr.inventory.hosts)
print("After setting password: ", nr.inventory.defaults.password)
test_file = 'test_file4.txt'

result = nr.run(task=netmiko_send_config, config_commands="ip scp server enable")
pprint(result['ACC-1'][0].result)


result = nr.run(
    task=netmiko_file_transfer,
    source_file=test_file,
    dest_file=test_file,
    direction='put',
    num_workers=20,
)
print_result(result)



"""
result = nr.run(napalm_get, getters=['get_interfaces'])

print_result(result)

for device in result.items():
    for interface in device[1].result['get_interfaces_counters'].items():
     if interface[1]['rx_octets'] :
         print("{} {} rx octets: {}".format(device[0], interface[0], interface[1]['rx_octets']))

result = nr.run(napalm_get, getters=['get_route_to'], getters_options={"get_route_to" : {'destination' : '192.168.10.12'}})
print(result['rtr1'][0].result['get_route_to'])


result = nr.run(task=netmiko_send_command, command_string="show version")
pprint(result['rtr1'][0].result)

"""