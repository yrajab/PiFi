from os import W_OK
import PingResult
import PushResult
import WiFiResult


target_address = "10.69.13.100"
interval = 0.1
timeout = 0.5
seconds = 60
payload_size = 512 #default 56

count = PingResult.count_calc(target_address, seconds, interval)

while(True):
    result = PingResult.ping_result(target_address, count, interval, timeout, payload_size)
    wifi_stats = WiFiResult.wifi_result()
    prtg_push = PushResult.push_result(count, result, wifi_stats)