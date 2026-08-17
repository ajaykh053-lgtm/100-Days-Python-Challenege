from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = float(os.environ["PROMISED_DOWN"])
PROMISED_UP = float(os.environ["PROMISED_UP"])

bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
try:
    download_el, upload_el = bot.get_internet_speed()

    # .text gives something like "45.3" — float() converts it
    download_speed = float(download_el.text)
    upload_speed = float(upload_el.text)

    print(f"Download : {download_speed} Mbps  (promised {PROMISED_DOWN})")
    print(f"Upload   : {upload_speed} Mbps  (promised {PROMISED_UP})")

    if download_speed < PROMISED_DOWN or upload_speed < PROMISED_UP:
        isp_handle = os.environ["X_HANDLE"]
        message = (
            f"Hey {isp_handle}! You promised {PROMISED_DOWN:.0f}Mbps down / "
            f"{PROMISED_UP:.0f}Mbps up. Right now I'm only getting "
            f"{download_speed}Mbps down / {upload_speed}Mbps up. "
            f"Fix this! 😤 #SlowInternet"
        )
        print(f"Speed below threshold — posting complaint:\n{message}")
        bot.tweet_at_provider(message)
    else:
        print("Speed is within promised range. No tweet needed.")

except Exception as e:
    print(f"❌ Bot crashed: {e}")
    raise
