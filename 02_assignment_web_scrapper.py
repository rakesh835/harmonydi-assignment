import requests
from bs4 import BeautifulSoup


URL = "https://www.cricbuzz.com/"
req = requests.get(URL)


soup = BeautifulSoup(req.text, 'html5lib') # html5lib is html parser
#print(soup.prettify())

# get ul tag within which all current matches are availabel
# on home page
matches_list = soup.find('ul', attrs = {'class': 'cb-col cb-col-100 videos-carousal-wrapper cb-mtch-crd-rt-itm'})


# get individual li tag of every single match 
all_matches = matches_list.findAll('li')

# Now we have individual li tag we need to parse inside nested tags to get the score and 
# team name


for match in all_matches:
	for sibling in match.a.div.find_next_sibling('div'):
		print(sibling.text)
		print("-----")


# This program still giving team name, team score, and also
# who won the match. But still need little more work. to get
# what exactly we nedd.
	



 