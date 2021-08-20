import json
import urllib3
from icmplib import ping

def count_calc(ip, sec):
    #calculate count for sec amount of seconds  worth of pings
    #ping the address with 4 pings, get the avg_rtt and calculate number of pings
    data = ping(ip)
    avg_rtt = data.avg_rtt
    ping_count_per_minute = int((sec*1000)/avg_rtt)
    return(ping_count_per_minute)


target_address = "10.168.13.100"
interval = 0.1
timeout = 0.5
seconds = 6
count = count_calc(target_address, seconds)
result = ping(target_address, count=count, interval=interval, timeout=timeout, privileged=True)
print("avg rtt =", result.avg_rtt)
print("min rtt =", result.min_rtt)
print("max rtt =", result.max_rtt)
print("packet loss =", result.packet_loss)
print("jitter =", result.jitter)