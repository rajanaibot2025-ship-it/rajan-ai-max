# ✅ Final Smart Quotex Login with Cookie Save (AI Stabilized)
import time, json, os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def smart_login():
    print("\n🔐 Launching secure Chrome window for Quotex login...")

    try:
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        
        # Smart driver startup with retry
        for attempt in range(3):
            try:
                driver = uc.Chrome(options=options)
                break
            except Exception as e:
                print(f"⚠️ Attempt {attempt+1} failed to start browser. Retrying...")
                time.sleep(2)
        else:
            print("❌ Unable to start Chrome browser.")
            return

        driver.get("https://quotex.com/en/sign-in")
        print("🕒 Please login manually within 2 minutes (120 seconds)...")

        # Smart login checker
        timeout = time.time() + 120
        logged_in = False
        while time.time() < timeout:
            current_url = driver.current_url
            if "trade" in current_url or "platform" in current_url:
                print("✅ Login detected! Saving cookies...")
                logged_in = True
                break
            time.sleep(1)

        if not logged_in:
            print("⛔ Timeout: Login not detected. Exiting safely.")
            driver.quit()
            return

        # Save cookies after successful login
        cookies = driver.get_cookies()
        with open("cookies.json", "w") as file:
            json.dump(cookies, file, indent=4)
        print("🍪 Cookies saved to 'cookies.json' successfully!")

    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")

    finally:
        try:
            driver.quit()
        except:
            pass
        print("🧹 Browser session closed cleanly.")

# ✅ Run directly
if __name__ == "__main__":
    smart_login()

