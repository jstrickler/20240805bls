### NOTE: THIS IS A WORK IN PROGRESS, AND WILL NOT WORK AS WRITTEN ###
import requests
# import bs4

URL = "https://www.cnn.com/2024/08/07/media/right-wing-media-tim-walz-harris-attacks-vp-election/index.html"

response = requests.get(URL)

if response.ok:
    page_text = response.text
    soup = bs4.soup(page_text)
    soup.find('some tag..."')
    if "Walz" in page_text:
        print("FOUND")
    else:
        print("NOT FOUND")