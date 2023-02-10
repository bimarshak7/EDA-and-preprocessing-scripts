'''
script to scrape news data from setopati and save in csv format
data scraped:
    - Title
    - Published Date
    - News Content
'''

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sys

def dig(start_page,end_page):
  file = open('/content/drive/MyDrive/NLP/news_data.csv','a')
  size = file.tell()
  if(size==0):
    file.write("id|date_published|title|news\n")

  print("Lets dig up setopati")
  print(f"Scraping page between {start_page} and {end_page}")

  c=0
  try:
    for j in range(start_page,end_page+1):
      res=requests.get(f"https://www.setopati.com/news/{j}").text
      soup = BeautifulSoup(res, 'html.parser')
      
      try:
        title = soup.find('span',class_="news-big-title").text
        news = soup.find('div', class_='editor-box').find_all('p')
        pub_date = soup.find('span',class_="pub-date").text
      except:
        continue

      title = title.replace("\n","")
      contents = "".join([ x.text.replace("\n"," ").replace("\t"," ") for x in news if len(x.text)>5])
      pub_date = pub_date.split(":")[1].strip().split()[0]
      
      #write in csv
      if len(contents)>20:
        file.write(f"{j}¬{pub_date}¬{title}¬{contents},\n")
      c+=1
      print(f"\rDone writting {c} news, Current page: {j}",end="")
  except Exception as exp:
      print("Error:: ",exp)
  finally:
      now = datetime.now()
      countFile = open("/content/drive/MyDrive/NLP/countCsv.txt","a")
      countFile.write(f"Last page = {j} scraped at {now.year}/{now.month}/{now.day}  {now.hour}:{now.minute}, Total news: {c}\n")
      countFile.close()
  print(f"\nTotal news: ",c)

  file.close()

if __name__=="__main__":
  start_page = int(sys.argv[1]) or 0
  end_page = int(sys.argv[2]) or 100
  dig(start_page,end_page)
