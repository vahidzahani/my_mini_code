import time
import requests
import platform

CHECK_INTERVAL = 30  # seconds


def check_ip():
    try:
        response = requests.get("https://ipapi.co/json/", timeout=10)
        data = response.json()

        ip = data.get("ip")
        country = data.get("country_code")
        country_name = data.get("country_name")

        print(f"IP: {ip} | Country: {country_name} ({country})")

        if country == "IR":
            print("\a" + "⚠️ ALERT: IP is from IRAN! ⚠️")
            return True

    except requests.RequestException as e:
        print(f"Error checking IP: {e}")

    return False


while True:
    is_iran = check_ip()

    if is_iran:
        # صدای Ding در ویندوز
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            # صدای بوق در Linux/macOS (در صورت پشتیبانی ترمینال)
            print("\a", end="", flush=True)

    time.sleep(CHECK_INTERVAL)