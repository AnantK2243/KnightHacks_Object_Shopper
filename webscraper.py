import requests
from bs4 import BeautifulSoup

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

    c = 0
    try:
        tempTitles = soup.find_all("span",{"class":"a-size-base-plus a-color-base a-text-normal"})
    except:
        tempTitles = (None)

    for i in tempTitles:
        for j in i:
            if(c!=10):
                titles.append(j)
                c+=1
    c = 0

    try:
        tempPrice = soup.find_all("span",{"class":"a-offscreen"})
    except:
        tempPrice = (None)

    for i in tempPrice:
        for j in i:
            if(c!=10):
                price.append(j)
                c+=1
    c = 0
    
    try:
        tempRating = soup.find_all("span",{"class":"a-icon-alt"})
    except:
        tempRating = (None)

    for i in tempRating:
        for j in i:
            if(c!=10):
                starRating.append(j)
                c+=1

    returnFile = []
    returnFile.append(titles)
    returnFile.append(price)
    returnFile.append(starRating)

    return returnFile

def main():   
    get_page_content("TV")

if __name__ == "__main__":
    main()

