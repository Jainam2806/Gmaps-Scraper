from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

def scrape_google_maps(query):
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
    for i in range(3,12,2):
        item = driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{i}]')
        innertText = item.get_attribute('innerText')
        results.append(innertText)
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
        main(query)
        return
    else:
        print(results)
        
if __name__ == "__main__":
    query = input("Search Query: ")
    main(query)