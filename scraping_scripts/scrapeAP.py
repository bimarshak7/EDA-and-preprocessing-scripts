from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sys

def dig_ap(start_page,end_page):
	base_url = "https://annapurnapost.com/"
	c=0
	print("Lets dig up annapurna post")
	print(f"Scraping page between {start_page} and {end_page}")

	file = open('/content/drive/MyDrive/NLP/ap.csv','a')
	size = file.tell()
	if(size==0):
  		file.write("id~#date_published~#title~#news\n")
	
	c = 0
	
	try:
		for i in range(start_page,end_page+1):
			page = requests.get(f"{base_url}/category/sampurna/?page={i}").text
			soup_ap = BeautifulSoup(page, 'html.parser')
			ap_news = soup_ap.find_all('h3', class_='card__title')

			for news in ap_news:
				url=news.find('a')['href']
				
				resSingle = requests.get(base_url+url).text
				soup = BeautifulSoup(resSingle, 'lxml')
				pub_date = soup.find('p',class_='date').find('span').text				
				title = soup.find('h1',class_='news__title').text.strip()
				news = soup.find('div',class_='news__details').find_all('p')

				news = "".join([ x.text.replace("\n"," ").replace("\t"," ") for x in news if len(x.text)>30])

				story_id = url.split("/")[2]
				if len(news)>20:
					file.write(f"{story_id}p{i}~#{pub_date}~#{title}~#{news},\n")
				c+=1
				print(f"\rDone writting {c} news, Current page: {i}",end="")

	except Exception as err:
		print("Error ",err)
	finally:
      now = datetime.now()
      countFile = open("/content/drive/MyDrive/NLP/countAP.txt","a")
      countFile.write(f"Last page = {j} scraped at {now.year}/{now.month}/{now.day}  {now.hour}:{now.minute}, Total news: {c}\n")
      countFile.close()

    print(f"\nTotal news: ",c)

if __name__=="__main__":
  start_page = int(sys.argv[1]) or 0
  end_page = int(sys.argv[2]) or 100
  dig_ap(start_page,end_page)
