"""
Scrape Los Angeles County's procurement portal for new opportunities.
"""

import requests
from bs4 import BeautifulSoup

LA_COUNTY_BIDS_URL = "https://camisvr.co.la.ca.us/lacobids/BidLookUp/BidOpenStart.asp"

def fetch_la_county_bids():
    response = requests.get(LA_COUNTY_BIDS_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    # Placeholder: Update selectors for live portal
    bid_table = soup.find("table", {"id": "bidTable"})
    bids = []
    if bid_table:
        for row in bid_table.find_all("tr")[1:]:
            cells = row.find_all("td")
            bid = {
                "title": cells[0].text.strip(),
                "due_date": cells[1].text.strip(),
                "url": cells[0].find("a")["href"]
            }
            bids.append(bid)
    return bids

if __name__ == "__main__":
    for bid in fetch_la_county_bids():
        print(bid)
