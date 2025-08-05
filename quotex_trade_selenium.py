from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

def place_trade_selenium(pair="eurusd", action="buy", duration="60", amount="10"):
    print("🚀 Launching Quotex for auto trade...")

    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=options)

    driver.get("https://quotex.com/en/trade")

    print("🕒 Please login manually within 60 seconds...")
    time.sleep(60)  # Wait for login manually

    try:
        # Open desired trading pair
        print(f"🔁 Opening pair: {pair.upper()}")
        driver.get(f"https://quotex.com/en/trade/{pair.lower()}")
        time.sleep(5)

        # Amount field
        print(f"💰 Entering amount: {amount}")
        amount_field = driver.find_element(By.CSS_SELECTOR, "input[name='amount']")
        amount_field.clear()
        amount_field.send_keys(str(amount))
        time.sleep(1)

        # Set duration
        print(f"⏳ Setting duration: {duration}s")
        duration_btn = driver.find_element(By.CSS_SELECTOR, f"button[data-time='{duration}']")
        duration_btn.click()
        time.sleep(1)

        # Click buy/sell
        if action == "buy":
            print("📈 Clicking BUY")
            driver.find_element(By.CLASS_NAME, "btn-up").click()
        else:
            print("📉 Clicking SELL")
            driver.find_element(By.CLASS_NAME, "btn-down").click()

        print(f"✅ Trade Placed: {pair.upper()} | {action.upper()} | ₹{amount}")
    except Exception as e:
        print("❌ Trade Error:", e)
    finally:
        time.sleep(10)
        driver.quit()

# 🧪 Test Run
place_trade_selenium("eurusd", "buy", "60", "10")

