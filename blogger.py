import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def random_scroll(url):
    try:
        chrome_options = Options()
        # chrome_options.add_argument('--proxy-server=http://your-proxy-server:port')
        driver = webdriver.Chrome()

        driver.get(url)
        wait = WebDriverWait(driver, 50)

        time.sleep(random.randint(5, 15)) # sleep randomly from 5 to 15 seconds

        scroll_pause_time = random.randint(2,10) # you can set your own pause time. My example is 1 second for each scroll attempt

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        time.sleep(5) # wait for 1 second before closing the driver
        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

websites = ["https://ilpd-ms.blogspot.com/2023/10/tips-to-master-english.html", 
"https://ilpd-ms.blogspot.com/2023/08/the-rise-of-lgs-revolutionary-approach.html", 
"https://ilpd-ms.blogspot.com/2023/07/which-sentence-is-correct.html"]
start_time = time.time()

while True:
    for url in websites:
        random_scroll(url)

    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time >= 3600: # replace 3600 with your desired duration in seconds
        break