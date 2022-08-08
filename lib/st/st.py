from array import array
import requests
from lib.broker import Broker
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from .st_parser import StParser

load_dotenv()


class St(Broker):
    def __init__(self) -> None:
        super().__init__()
        self._raw_url = os.getenv("ST_URL_RAW")

    def pull_bets(self):
        full_html = requests.get(self._raw_url)
        soup = BeautifulSoup(full_html.text, "html.parser")

        football_category = soup.find(id="sport_184")
        league_links = self._get_league_links(football_category)
        # TODO: make loop
        match_details_links = self._get_match_detail_link(league_links[0])

        # for detail_link in match_details_links:
        detail_data = self._req_detail(match_details_links[0])
        # soup = BeautifulSoup(detail_data.text, "html.parser")

        StParser().parse(detail_data.text)

        # print(str(league_links))

        # print(match_pages)

        # soup2 = BeautifulSoup(match_pages[0].text, "html.parser")
        # print(soup2)

        # es = requests.get(
        #     "{}/{}".format(
        #         self._raw_url,
        #         "/pl/zaklady-bukmacherskie/pilka-nozna/estonia/184/30898/",
        #     )
        # )
        # esSoup = BeautifulSoup(match_pages[0].text, "html.parser")
        # ess = esSoup.find(id="offerTables")
        # for bets in ess.find_all("td", {"class": "support_bets"}):
        #     print(bets.find("a").get("href"))

        # es1 = requests.get(
        #     "{}/{}".format(
        #         self._raw_url,
        #         "/pl/zaklady-bukmacherskie/pilka-nozna/polska/ekstraklasa/w-plock-legnica/184/30860/86441/471999260/",
        #     )
        # )
        # print(
        #     "{}/{}".format(
        #         self._raw_url,
        #         "/pl/zaklady-bukmacherskie/pilka-nozna/polska/ekstraklasa/w-plock-legnica/184/30860/86441/471999260/",
        #     )
        # )

        # pattern = re.compile("zakład bez remisu")
        # esSoup2 = BeautifulSoup(es1.text, "html.parser")

        # # xs = esSoup2.prettify()
        # s = esSoup2.find_all("span", {"class": "liga"})
        # # print(s.getText())
        # # print(xs)
        # for xd in s:
        #     print(xd.getText())
        # # z = "zakład bez remisu"
        # # ess1 = esSoup2.find()

    # def _get_match_detail_link(self, match_link):
    #     # soup = BeautifulSoup(html_element.text, "html.parser")
    #     # print(soup.text)
    #     page = self._req_detail(match_link)
    #     soup = BeautifulSoup(page.text, "html.parser")

    #     soup.find_all("span", {"class": "liga"})

    def _get_match_detail_link(self, league_link) -> array:
        links = []
        page = self._req_detail_league(league_link)
        soup = BeautifulSoup(page.text, "html.parser")

        # Main table with bets in current league
        main_table = soup.find(id="offerTables")

        # "support_bets" means button html tag id with more bets of match.
        for href_link in main_table.find_all("td", {"class": "support_bets"}):
            links.append(href_link.find("a").get("href"))

        return links

    def _get_league_links(self, html_element) -> array:
        match_links = []
        for league in html_element.find_all("a"):
            match_links.append(league.get("href"))

        return match_links

    def _req_detail_league(self, link) -> str:
        return self._req_detail(link)

    def _req_detail_match(self, link) -> str:
        return self._req_detail(link)

    def _req_detail(self, link) -> str:
        return requests.get("{}/{}".format(self._raw_url, link))
