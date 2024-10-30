import winsound
import time
from datetime import datetime

def beep_on_five_minute_intervals():
    winsound.Beep(1000, 500)
    while True:
        # گرفتن زمان فعلی سیستم
        current_time = datetime.now()
        current_minute = current_time.minute
        print(current_time)

        # بررسی اینکه دقیقه فعلی مضربی از 5 باشد
        if current_minute % 5 == 0:
            # پخش صدای بوق (فرکانس 1000 هرتز به مدت 500 میلی‌ثانیه)
            winsound.Beep(1000, 500)

            # منتظر ماندن برای 60 ثانیه تا دوباره همان دقیقه بوق نزند
            time.sleep(60)
        else:
            # اگر دقیقه فعلی مضربی از 5 نبود، 10 ثانیه صبر کند و دوباره چک کند
            time.sleep(10)

# اجرای تابع
beep_on_five_minute_intervals()
