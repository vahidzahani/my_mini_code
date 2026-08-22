import requests
import subprocess
import time

INTERVAL = 5
previous_ip = None

while True:
    try:
        data = requests.get(
            "https://ipinfo.io/json",
            timeout=3
        ).json()

        ip = data.get("ip", "N/A")
        country = data.get("country", "N/A")

    except:
        ip = "N/A"
        country = "N/A"

    try:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "2000", "1.1.1.1"],
            capture_output=True,
            text=True
        )

        ping = "DOWN"

        for line in result.stdout.splitlines():
            if "time=" in line.lower():
                ping = line.lower().split("time=")[1].split("ms")[0]
                ping = ping.strip() + "ms"
                break

    except:
        ping = "DOWN"

    print(f"PING: {ping} | IP: {ip} | COUNTRY: {country}")

    # Beep once when IP changes
    if previous_ip is not None and ip != previous_ip:
        print("\a", end="", flush=True)

    previous_ip = ip

    time.sleep(INTERVAL)