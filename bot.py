from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()
driver.implicitly_wait(5)

data = dict()
driver.get('https://www.youtube.com/results?search_query=science+and+knowledge')
curr = dict()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, r'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/div[1]/ytd-search-header-renderer/div[1]/yt-chip-cloud-renderer/div/div[2]/iron-selector/yt-chip-cloud-chip-renderer[3]/div/chip-shape/button').click()

time.sleep(10)
t = input("Enter the input : ")
anchors = driver.find_elements(By.ID, 'thumbnail')
images = driver.find_elements(By.XPATH, '//*[@id="thumbnail"]/yt-image/img')
titles = driver.find_elements(By.ID, "video-title")
channel_links = driver.find_elements(By.ID, "channel-thumbnail")
channel_names = driver.find_elements(By.ID, "text-container")
video_details = driver.find_elements(By.ID, "metadata-line")
channel_thumbnails = driver.find_elements(By.XPATH, '//*[@id="img"]')
print(len(anchors))
print(len(images))
print(len(titles))
print(len(channel_links))
print(len(channel_names))
print(len(video_details))
print(len(channel_thumbnails))
po =0
for channel in channel_thumbnails:
    if channel.get_attribute('src'):
        po+=1
print("po = " + str(po))
j=1
k=-1
po = 0
for anchor in anchors:
    curr = dict()
    link = anchor.get_attribute('href')
    if link is not None:
        curr['video-link'] = link
        img = images[j-1].get_attribute("src")
        title = titles[j-1].get_attribute("title")
        curr['img-link'] = str(img)
        curr['title'] = str(title)
        curr['channel-link'] = channel_links[j-1].get_attribute('href')
        txt = ""
        while txt=="" and k<len(channel_names)-1:
            k+=1
            txt = channel_names[k].text
            if curr['title'] == "Why everything in science is connected - BBC World Service":
                curr['channel-name'] = 'BBC World Service'
                break
        curr['channel-name'] = txt
        curr['video-details'] = video_details[j-1].text.replace('\n', ' \u00B7 ')
        nail = ""
        while nail=="" and nail!=None and po<len(channel_thumbnails):
            nail = channel_thumbnails[po].get_attribute("src")
            po+=1

        curr['channel-img'] = nail
        k+=1
        data[j] = curr
        j+=1



print(data)

with open('data2.json', 'w') as file:
    json.dump(data, file, indent=4)

time.sleep(10000000)
