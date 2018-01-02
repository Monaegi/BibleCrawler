from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://maria.catholic.or.kr/bible/read/bible_read.asp'
PAYLOAD = {
    'm': 2,  # 1: 구약성경, 2: 신약성경 ...
    'n': 147,  # 전체 성경 각 권의 pk 값
    'p': 1,  # 페이지
}


def requests_from_catholic_goodnews(url, payload):
    """
    가톨릭 굿뉴스 사이트에서 리퀘스트 객체를 받아온다
    :param url: request를 받을 url
    :param payload: parameter 값
    :return: requests 객체
    """
    return requests.get(url, params=payload)


def soup_from_requests(requests):
    """
    리퀘스트 객체에서 soup 객체를 받아온다
    :param requests: requests 객체
    :return: soup 객체
    """
    text = requests.text
    return BeautifulSoup(text, 'lxml')


def texts_from_soup(soup):
    """
    soup 객체에서 성경 구절 텍스트 리스트를 받아온다
    :param soup: soup 객체
    :return: 성경 구절 리스트
    """
    texts = soup.select_one('#container > .type3 > #scrapSend > #font_chg > tbody')
    li = texts.find_all('td', attrs={'class': 'tt'})
    return [i.text.strip() for i in li]


if __name__ == '__main__':
    r = requests_from_catholic_goodnews(BASE_URL, PAYLOAD)
    print(r)
    s = soup_from_requests(r)
    # print(s)
    t = texts_from_soup(s)
    print(t)
