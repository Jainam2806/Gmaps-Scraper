import time
from selenium import webdriver
from webdriver.common.by import By
from webdriver.common.service import Service
from webdriver.common.keys import Keys
from webdriver.manager.chrome import ChromeDriverManager
from webdriver.chrome.options import Options as ChromeOptions

def scrape_google_maps(query):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage") 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.google.com/maps")
    time.sleep(1.5)
    
    search_box = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(1.5)
    for _ in range(9):
        try:
            driver.execute_script(f"""document.querySelector('[aria-label="Results for {query}"]').scrollTop = document.querySelector('[aria-label="Results for {query}"]').scrollHeight;""")
        except:
            return(scrape_google_maps(query))
        time.sleep(2.5)
  
    results = []
    for i in range(3,102,2):
        try:
            item = driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{i}]')
            innertText = item.get_attribute('innerText')
            results.append(innertText)
        except:
            continue
    driver.quit()
    return results

def format_output(data):
    shop_details = {}
    for index,i in enumerate(data):
        shop_name = i.split('\n')[0]
        try:
            shop_address = i.split('\n')[2]
        except:
            shop_address = None
        if shop_address is not None:
            try:
                shop_phone = int(i.split('\n')[3][-11:-6]+i.split('\n')[3][-5:])
            except:
                try:
                    shop_phone = int(i.split('\n')[3][-13:-10]+i.split('\n')[3][-9:-5]+i.split('\n')[3][-4:])
                except:
                    shop_phone = None
        else:
            shop_phone = None
        shop_details[index+1] = {"shop_name":shop_name,"shop_address":shop_address,"shop_phone":shop_phone}    
    return shop_details

def main(query):
    results = scrape_google_maps(query)
    results = format_output(results)
    if results[2]['shop_name'] == '':
        result = results[1]['shop_name'].split(' ')
        query = result[3]+' '+result[4]+' '+result[5]+' '+result[6]
        results = main(query)
        return results
    else:
        return results