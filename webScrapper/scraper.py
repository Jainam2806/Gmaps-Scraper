from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

def scrape_google_maps(query):
    """
    Function to scrape Google Maps for a given query.

    Args:
    query (str): The search query for Google Maps.

    Returns:
    None
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com/maps")
    time.sleep(2)
    
    search_box = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    for _ in range(9):
        driver.execute_script(f"""document.querySelector('[aria-label="Results for {query}"]').scrollTop = document.querySelector('[aria-label="Results for {query}"]').scrollHeight;""")
        time.sleep(3)
  
    results = []
    for i in range(3,102,2):
        item = driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{i}]')
        innertText = item.get_attribute('innerText')
        
        print(innertText)
        print("______________________________________________________________________________________________________")
        results.append(innertText)
    driver.quit()
    # return results

query = input("Search Query: ")
scrape_google_maps(query)
# results = scrape_google_maps(query)
# print(results)