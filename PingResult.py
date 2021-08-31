from icmplib import ping

def count_calc(ip, sec, int):
    #calculate count for sec amount of seconds  worth of pings
    #ping the address with 4 pings, get the avg_rtt and calculate number of pings
    data = ping(ip)
    avg_rtt = data.avg_rtt
    if avg_rtt == 0.0: return()
    pings = ((sec*1000)/(avg_rtt + (int*1000)))
    ping_count_per_minute = pings.__round__()
    return(ping_count_per_minute)

def ping_result(target_address, count, interval, timeout, payload_size):
    result = ping(target_address, count=count, interval=interval, timeout=timeout, privileged=True, payload_size=payload_size)
    return(result)