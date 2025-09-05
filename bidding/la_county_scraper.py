import requests
from bs4 import BeautifulSoup

def fetch_la_county_bids():
    url = "https://camisvr.co.la.ca.us/lacobids"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    bids = []
    # Find the table body by its unique id
    tbody = soup.find("tbody", id="searchTbl1")
    if not tbody:
        print("No bids table found.")
        return bids

    for row in tbody.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) < 5:
            continue  # Skip malformed rows

        # 1. Solicitation Number and hidden bid ID (from selectBid)
        num_link = cols[0].find("a")
        solicitation_number = num_link.get_text(strip=True) if num_link else ""
        bid_id = ""
        if num_link and num_link.has_attr("href"):
            # Extract bid ID from javascript:selectBid('...')
            import re
            match = re.search(r"selectBid\('(\d+)'\)", num_link["href"])
            if match:
                bid_id = match.group(1)

        # 2. Title
        title_label = cols[1].find("label", {"name": "BidTitleEllipsis"})
        title = title_label.get_text(strip=True) if title_label else ""

        # 3. Type
        bid_type = cols[2].get_text(strip=True)

        # 4. Department
        department = cols[3].get_text(strip=True)

        # 5. Close Date
        close_date = cols[4].get_text(strip=True)

        # 6. Commodity (optional, from label inside column 2)
        comm_label = cols[1].find("label", {"name": "CommDescEllipsis"})
        commodity = ""
        if comm_label:
            # Remove "Commodity:" prefix if present
            commodity = comm_label.get_text(strip=True).replace("Commodity:", "").strip()

        bids.append({
            "solicitation_number": solicitation_number,
            "bid_id": bid_id,
            "title": title,
            "type": bid_type,
            "department": department,
            "close_date": close_date,
            "commodity": commodity
        })

    print(f"Number of bids found: {len(bids)}")
    for bid in bids:
        print(bid)
    return bids

if __name__ == "__main__":
    fetch_la_county_bids()