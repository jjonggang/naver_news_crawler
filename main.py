import requests
from bs4 import BeautifulSoup

titles = []  # 뉴스기사 제목이 들어갈 배열 (필요한 경우 사용)
links = []  # 링크가 들어갈 배열


def find_news(search_word, page):

    news_page = page*16

    url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_pge&query={search_word}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=101&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start={news_page}'

    req = requests.get(url)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')  # html 클래스 별로 가져올 수 있도록 한다.

    search_result = soup.select_one('#news_result_list')

    news_title = search_result.select('.bx > .news_wrap > a')

    for title in news_title:
        news_page = news_page+1
        titles.append(title.get_text())
        links.append(title['href'])
        # print('순번: '+str(news_page))
        print('제목:'+title.get_text())
        print('링크: '+title['href'])


while 1:
    search_word = input('찾고 싶은 기사 주제를 입력하세요: ')
    page = 0
    find_news(search_word, page)
    while 1:
        option = input('1. 기사 추가 로드 \n2. 다른 기사 검색 \n3. 프로그램 종료\n: ')
        if option == '1':
            page = page+1
            find_news(search_word, page)
        elif option == '2':
            titles.clear()
            links.clear()
            break
        else:
            quit()
