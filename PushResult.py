import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def push_result(count, result, wifi_stats):

    url = "http://10.168.70.206:5050/"
    http_headers = {}
    http_headers["accept"] = "application/json; charset=ISO-8859-1;"
    token = "5FA6A5E4-2F69-4545-8600-F8FDF121BAD3"

    output_json = {
        "prtg": {
            "text": "OK",
            "result": [
                {
                    "channel": "Pings Sent",
                    "value": count,
                    "float": "0",
                    "unit": "Count",
                },
                {
                    "channel": "Average RTT",
                    "value": result.avg_rtt,
                    "float": "1",
                    "unit": "Custom",
                    "customunit": "ms"
                },
                {
                    "channel": "Max RTT",
                    "value": result.max_rtt,
                    "float": "1",
                    "unit": "Custom",
                    "customunit": "ms"
                },
                {
                    "channel": "Min RTT",
                    "value": result.min_rtt,
                    "float": "1",
                    "unit": "Custom",
                    "customunit": "ms"
                },
                {
                    "channel": "Packet Loss",
                    "value": (result.packet_loss*100),
                    "float": "1",
                    "unit": "Percent"
                },
                {
                    "channel": "Jitter",
                    "value": result.jitter,
                    "float": "1",
                    "unit": "Custom",
                    "customunit": "ms"
                },
                {
                    "channel": "Rate",
                    "value": wifi_stats["Rate"],
                    "float": "0",
                    "unit": "Custom",
                    "customunit": "Mb/s"
                },
                {
                    "channel": "TX Level",
                    "value": wifi_stats["TXPower"],
                    "float": "0",
                    "unit": "Custom",
                    "customunit": "dBm"
                },
                {
                    "channel": "Quality",
                    "value": wifi_stats["Quality"],
                    "float": "0",
                    "unit": "Percent"
                },
                {
                    "channel": "Signal Level",
                    "value": wifi_stats["Level"],
                    "float": "0",
                    "unit": "Custom",
                    "customunit": "dBm"
                },
                {
                    "channel": "Frequency",
                    "value": wifi_stats["Frequency"],
                    "float": "1",
                    "unit": "Custom",
                    "customunit": "GHz"
                },
                {
                    "channel": "Channel",
                    "value": wifi_stats["Channel"],
                    "float": "0",
                    "unit": "Custom",
                    "customunit": "Ch#"
                }
            ]
        }
    }

    full_url = url + token + "?content=" + json.dumps(output_json)
    print(full_url)
    try:
        r = requests.get(full_url, headers=http_headers, verify=False)
        return(r)
    except Exception as e:
        print(e)