import requests
from bs4 import BeautifulSoup

# Step 2. Getting the content of the top n pages

def get_page_content(item):
    titles = []
    price = []
    starRating = []

    targetURL = 'https://www.amazon.com/s?k=' + item
    
    headers1 = {
        "accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    resp = requests.get(targetURL, headers=headers1)
    
    soup = BeautifulSoup(resp.text,'html.parser')

    try:
        tempTitles = soup.find_all("span",{"class":"a-size-medium a-color-base a-text-normal"})
    except:
        tempTitles = (None)

    for i in tempTitles:
        for j in i:
            titles.append(j)

    print(titles)

get_page_content("TV")