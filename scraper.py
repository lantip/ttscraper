import os
import time
from datetime import datetime, timedelta
from tqdm import tqdm
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from scrape_utils import ScrapeUtils, Wait
import downloader
from bs4 import BeautifulSoup
import json

def create_folder_if_not_exist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def scrape_video(driver, folder="./", tipe="username"):
    h2 = driver.find_elements_by_tag_name('h2')
    if tipe == 'username':
        text =  h2[6].text
    else:
        text = h2[4].text
    downloaded = False
    if "ago" in text:
        txt = text.split(' · ')
        if 'd' in txt[1]:
            tet = txt[1].split('d')[0]
            tgl = datetime.now() - timedelta(days=int(tet))
        elif 'h' in txt[1]:
            tet = txt[1].split('h')[0]
            tgl = datetime.now() - timedelta(hours=int(tet))
        else:
            tgl = datetime.now()
        url = driver.find_element_by_tag_name("video").get_attribute("src")
        name = "".join(url.split("/")[3:5])
        name = tgl.strftime('%Y-%m-%d')+"--"+name
        name = os.path.join(folder, name)
        
        downloaded = True
        downloader.download_mp4(name, url)    
         
    else:
        txt = text.split(' · ')
        if len(txt) > 1:
            if len(txt[1].strip()) > 1:
                url = driver.find_element_by_tag_name("video").get_attribute("src")
                name = "".join(url.split("/")[3:5])
                name = '20-'+txt[1]+"--"+name
                name = os.path.join(folder, name)
                
                downloaded = True
                downloader.download_mp4(name, url)
    
    clos =  driver.find_element_by_class_name('close')
    clos.click()

def start(driver, username, tipe='username', folder=None, delay=10):
    if folder is None:
        if tipe == 'username':
            folder = f"./{username}"
        else:
            folder = f"./tags-{username}"
        create_folder_if_not_exist(folder)
    if tipe  == 'username':
        url = f"https://www.tiktok.com/@{username}"
    else:
        url = f"https://www.tiktok.com/tag/{username}"
    driver.get(url)
    if not Wait(driver).for_class_name("video-feed"):
        raise Exception(f"Can't load {url}")

    print("Getting all videos...")
    ScrapeUtils.scroll_bottom(driver)
    
    main_elem = driver.find_element_by_tag_name("main")
    print("Preparing to download")
    
    for link in tqdm(main_elem.find_elements_by_tag_name("a"), desc=f"Downloading videos to {folder}"):
        print(link.text)
        try:
            link.click()
        except ElementClickInterceptedException:
            print("clicked")
        except:
            print("failed")
        else:
            scrape_video(driver, folder=folder, tipe=tipe)
        time.sleep(delay)
    
if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('user-agent=Naverbot')
    driver = webdriver.Chrome(options=chrome_options)
    start(driver, "kimnevri")
