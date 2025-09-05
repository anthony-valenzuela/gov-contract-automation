"""
Scrape Orange County's procurement portal for new opportunities.
"""

import requests
from bs4 import BeautifulSoup

OC_COUNTY_BIDS_URL = "https://olbidprocure.ocgov.com/Bids"

def fetch_oc_bids():
    response = requests.get(OC_COUNTY_BIDS_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    # Placeholder: Update selectors for live portal
    bid_table = soup.find("table", {"class": "bid-list"})
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
    for bid in fetch_oc_bids():
        print(bid)
