from django.shortcuts import render
import nmap
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def scan_network(network_range):
    nm = nmap.PortScanner()
    scan_results = nm.scan(hosts=network_range, arguments='-sP')

    devices = []

    for host in nm.all_hosts():
        # vendor_list = nm[host].get('vendor', [{'vendor': 'Unknown'}])
        # vendor = ', '.join([v.get('vendor', 'Unknown') for v in vendor_list])
        device_info = {
            'host': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state(),
            # 'vendor': vendor
        }
        devices.append(device_info)

    return devices





def network_scan_view(request):
    network_range = '192.168.54.0/24'
    devices = scan_network(network_range)
    return render(request, 'scan.html', {'devices': devices})
    
