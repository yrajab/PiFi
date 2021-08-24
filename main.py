import PingResult
import PushResult


target_address = "10.69.13.100"
interval = 0.1
timeout = 0.5
seconds = 150
payload_size = 512 #default 56

count = PingResult.count_calc(target_address, seconds, interval)
result = PingResult.ping_result(target_address, count, interval, timeout, payload_size)

prtg_push = PushResult.push_result(count, result)

print("Pings sent ", count)
print("avg rtt =", result.avg_rtt)
print("min rtt =", result.min_rtt)
print("max rtt =", result.max_rtt)
print("packet loss =", result.packet_loss)
print("jitter =", result.jitter)