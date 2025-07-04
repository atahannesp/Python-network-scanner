import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target",dest="target",help="Target IP / IP range.")
    (options, arguments) = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #ARP objesi
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #Ethernet objesi
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    if not results_list:
        print("No devices found on the network")
    else:
        print("{:<20} {:<}".format("IP", "MAC Address"))
        print("-" * 40)
        for client in results_list:
            print("{:<20} {:<}".format(client['ip'], client['mac']))

options = get_arguments()

if not options.target:
    print("[-] Please specify a target using -t or --target")
    exit()


scan_result = scan(options.target)

print_result(scan_result)
