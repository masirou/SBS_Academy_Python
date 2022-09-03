import requests
from bs4 import BeautifulSoup

# url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     ul = soup.select_one('ul.basic1')
#     titles = ul.select('li > dl > dt > a')
#     for title in titles:
#         print(title.get_text())
# else:
#     print(response.status_code)


resp = requests.get('https://kin.naver.com/')

bs = BeautifulSoup(resp.text, 'html.parser')
uls = bs.select_one('ul.ranking_list')
uls2 = bs.select_one('#rankingChart > ul:nth-child(2)')

titles = uls.select('li > a.ranking_title')
titles2 = uls2.select('li > a.ranking_title')
for idx, title in enumerate(titles):
    if idx >= 3:
        break
    print(idx+1, title.get_text())
for idx, title in enumerate(titles2):
    if idx >= 3:
        break
    print(idx+4, title.get_text())


# strongs = bs.find_all('strong', class_='rank_title')
# for idx, ul in enumerate(uls):
#     print(strongs[idx].text.strip())
#     lis = ul.find_all('li', class_='list')
#     for li in lis:
#         print(li.text.strip().split('\n'))\

# # + 각 날짜별로 새롭게 발생한 키워드
# # + 각 날짜별로 겹치는 키워드
