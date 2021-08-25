from os import W_OK
import PingResult
import PushResult
import WiFiResult


target_address = "192.168.1.1"
interval = 0.1
timeout = 0.5
seconds = 3
payload_size = 512 #default 56

count = PingResult.count_calc(target_address, seconds, interval)
result = PingResult.ping_result(target_address, count, interval, timeout, payload_size)
wifi_stats = WiFiResult.wifi_result()

prtg_push = PushResult.push_result(count, result, wifi_stats)

print("Pings sent ", count)
print("avg rtt =", result.avg_rtt)
print("min rtt =", result.min_rtt)
print("max rtt =", result.max_rtt)
print("packet loss =", result.packet_loss)
print("jitter =", result.jitter)