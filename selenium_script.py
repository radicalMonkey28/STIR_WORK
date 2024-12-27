from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pymongo
import uuid

# Configure Selenium with Proxy
def get_driver(proxy=None):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=options)
    return driver

# Fetch trending topics
def fetch_trending_topics():
    proxy = "http://your-proxy-mesh-url"  # Replace with ProxyMesh details
    driver = get_driver(proxy)
    try:
        driver.get("https://twitter.com/login")
        
        # Log in
        username = driver.find_element(By.NAME, "text")
        username.send_keys("your-email")
        username.send_keys(Keys.RETURN)
        time.sleep(2)
        
        password = driver.find_element(By.NAME, "password")
        password.send_keys("your-password")
        password.send_keys(Keys.RETURN)
        time.sleep(5)

        # Get trending topics
        trends = driver.find_elements(By.XPATH, '//div[@aria-label="Timeline: Trending now"]//span')[:5]
        trending_topics = [trend.text for trend in trends]
        driver.quit()

        # Return trending topics
        return trending_topics
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return []
