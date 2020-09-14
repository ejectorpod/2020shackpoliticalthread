import requests
import schedule
import time
from bs4 import BeautifulSoup
url = "https://whatthefuckjusthappenedtoday.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("main")

def tdget():
	post_elems = results.find_all("article", class_="post")

	for post_elem in post_elems:
		item_elem = post_elem.find("ol")
		if None in (item_elem):
			continue
		print(item_elem.text.strip())
		with open("trumpdump.txt", "w") as output:
			output.write(item_elem.text.strip())

schedule.every(24).hours.do(tdget)
schedule.every().day.at("22:30").do(tdget)

while 1:
		schedule.run_pending()
		time.sleep(1)
