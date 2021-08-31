import subprocess
import re

def wifi_result():
    stats={}
    data = str(subprocess.check_output(['iwconfig', 'wlan0']))
    R = re.search("Rate=(\d+)", data).group(1)
    stats["Rate"] = int(R)
    T = re.search("Power=(\d+)", data).group(1)
    stats["TXPower"] = int(T)
    Q = re.search("Quality=(\d+)", data).group(1)
    stats["Quality"] = round(((int(Q)/70)*100), 3)
    L = re.search("level=-(\d+)", data).group(1)
    stats["Level"] = (int(L))*(-1)

    data = str(subprocess.check_output(['iwlist', 'wlan0', 'scanning']))
    F = re.search("Frequency:(\d\.\d+)", data).group(1)
    stats["Frequency"] = float(F)
    C = re.search("Channel:(\d+)", data).group(1)
    stats["Channel"] = int(C)
    return(stats)