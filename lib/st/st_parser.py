from bs4 import BeautifulSoup

from lib.st.constant import ST_EVENT_ITEM_TYPES


class StParser:
    @classmethod
    def parse(cls, html_data):
        soup = BeautifulSoup(html_data, "html.parser")
        bet_tables = soup.find_all("span", {"class": "liga"})

        for table in bet_tables:
            cls.parse_table(table.parent.parent.parent.parent)

    @classmethod
    def parse_table(cls, table_element):
        event_tag = table_element.find("span", {"class": "liga"})
        event_name = event_tag.get_text().strip()

        for key, value in ST_EVENT_ITEM_TYPES.items():
            # print("-------")
            # print(value)
            # print(event_name)
            # print("-------")
            if value == event_name:
                cls.create_bet(key, event_tag)

    @classmethod
    def create_bet(cls, key, html_table) -> None:
        print(key)
        pass
