# ✅ fix_cookies.py
import json

def fix_cookies(file_path='cookies.json'):
    try:
        with open(file_path, 'r') as f:
            raw_cookies = json.load(f)

        # ✅ Small Brain Logic: Filter and fix cookie format
        fixed_cookies = {}
        for cookie in raw_cookies:
            if isinstance(cookie, dict) and 'name' in cookie and 'value' in cookie:
                fixed_cookies[cookie['name']] = cookie['value']
            else:
                print(f"⚠️ Skipping invalid cookie format: {cookie}")

        # Save fixed cookies to new file
        fixed_path = 'fixed_cookies.json'
        with open(fixed_path, 'w') as f:
            json.dump(fixed_cookies, f, indent=2)

        print(f"\n✅ Cookies fixed and saved to: {fixed_path}")
        print(f"🧠 Total valid cookies: {len(fixed_cookies)}")

    except FileNotFoundError:
        print(f"❌ Error: '{file_path}' file not found.")
    except json.JSONDecodeError:
        print(f"❌ Error: '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == '__main__':
    fix_cookies()

