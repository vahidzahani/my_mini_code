import winsound
import time
from datetime import datetime
import os

def set_terminal_color_blue_background_white_text():
    """
    Set Windows terminal background to blue and text to white.
    Equivalent to 'color 1F' in cmd.
    """
    os.system("color 1F")


def speaker():
    winsound.Beep(2000, 1000)
    winsound.Beep(1000, 300)
    winsound.Beep(1000, 100)
    winsound.Beep(1000, 300)
    winsound.Beep(1000, 300)
    winsound.Beep(1000, 300)
    winsound.Beep(1000, 300)


def beep_on_five_minute_intervals():
    speaker()  # Play test beep once at startup

    alerted = False  # Prevents repeated main beeps within same minute
    warned  = False  # Prevents repeated warning beeps within same minute

    while True:
        now    = datetime.now()
        minute = now.minute
        second = now.second
        print(now.strftime("%H:%M:%S"))

        # --- Warning beep: 10 seconds before a 5-minute mark ---
        if minute % 5 == 4 and second >= 50 and not warned:
            speaker()
            warned = True

        # --- Main beep: Exactly on the 5-minute mark (± 2 seconds) ---
        if minute % 5 == 0 and second < 3 and not alerted:
            #speaker()
            alerted = True
            warned = False  # Reset for the next cycle

        # --- Reset flags if not on a 5-minute mark anymore ---
        if minute % 5 != 0:
            alerted = False
            if minute % 5 != 4:
                warned = False

        time.sleep(1)  # CPU-friendly loop interval

# === Run the function with clean exit support ===
if __name__ == "__main__":
    try:
        set_terminal_color_blue_background_white_text()
        beep_on_five_minute_intervals()
    except KeyboardInterrupt:
        print("\nProgram terminated successfully.")
