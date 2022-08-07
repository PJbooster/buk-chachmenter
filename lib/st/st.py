from array import array
from pydoc import classname
import requests
from lib.broker import Broker
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import re

load_dotenv()


class St(Broker):
    def __init__(self) -> None:
        super().__init__()
        self._url = os.getenv("ST_URL")
        self._raw_url = os.getenv("ST_URL_RAW")

    def pull_bets(self):
        # full_html = requests.get(self._url)
        # soup = BeautifulSoup(full_html.text, "html.parser")

        # football_category = soup.find(id="sport_184")
        # match_pages = self._get_match_pages(football_category)

        # soup2 = BeautifulSoup(match_pages[0].text, "html.parser")
        # print(soup2.text)

        # es = requests.get(
        #     "{}/{}".format(
        #         self._raw_url,
        #         "/pl/zaklady-bukmacherskie/pilka-nozna/estonia/184/30898/",
        #     )
        # )
        # esSoup = BeautifulSoup(es.text, "html.parser")
        # ess = esSoup.find(id="offerTables")
        # for bets in ess.find_all("td", {"class": "support_bets"}):
        #     print(bets.find("a").get("href"))

        es1 = requests.get(
            "{}/{}".format(
                self._raw_url,
                "/pl/zaklady-bukmacherskie/pilka-nozna/estonia/1-liga/narva-levadia-tallin/184/30898/86771/472793123/",
            )
        )

        pattern = re.compile("zakład bez remisu")
        esSoup2 = BeautifulSoup(es1.text, "html.parser")

        s = esSoup2.find_all("span", {"class": "liga"})
        # print(s.getText())
        print(len(s))
        for xd in s:
            print(xd.getText())
        # z = "zakład bez remisu"
        # ess1 = esSoup2.find()

    def _get_match_details(self, html_element):
        soup = BeautifulSoup(html_element.text, "html.parser")
        print(soup.text)

    def _get_match_detail_links(self, league_link) -> array:
        links = []
        page = self._req_detail_league(league_link)
        soup = BeautifulSoup(page.text, "html.parser")

        # Main table with bets in current league
        main_table = soup.find(id="offerTables")

        # "support_bets" means button html tag id with more bets of match.
        for href_link in main_table.find_all("td", {"class": "support_bets"}):
            links.append(href_link.find("a").get("href"))

        return links

    def _get_match_pages(self, html_element) -> array:
        match_pages = []
        for league in html_element.find_all("a"):
            match_pages.append(self._req_detail_league(league.get("href")))

        return match_pages

    def _req_detail_league(self, link) -> str:
        return self._req_detail(link)

    def _req_detail_match(self, link) -> str:
        return self._req_detail(link)

    def _req_detail(self, link) -> str:
        return requests.get("{}/{}".format(self._raw_url, link))
