import json
import urllib3
from icmplib import ping
from datetime import datetime

def count_calc(ip, sec, int):
    #calculate count for sec amount of seconds  worth of pings
    #ping the address with 4 pings, get the avg_rtt and calculate number of pings
    data = ping(ip)
    avg_rtt = data.avg_rtt
    if avg_rtt == 0.0: return()
    pings = ((sec*1000)/(avg_rtt + (int*1000)))
    ping_count_per_minute = pings.__round__()
    return(ping_count_per_minute)

target_address = "10.69.13.100"
interval = 0.1
timeout = 0.5
seconds = 3
payload_size = 512 #default 56
count = count_calc(target_address, seconds, interval)
start = datetime.now()
result = ping(target_address, count=count, interval=interval, timeout=timeout, privileged=True, payload_size=payload_size)
print("Pings sent ", count)
print("avg rtt =", result.avg_rtt)
print("min rtt =", result.min_rtt)
print("max rtt =", result.max_rtt)
print("packet loss =", result.packet_loss)
print("jitter =", result.jitter)
print("Execution time = ", (datetime.now()-start))