import requests
import csv
from bs4 import BeautifulSoup

all_quotes = []

for page in range(1, 11):

    url = f"https://quotes.toscrape.com/page/{page}/"

    print(f"Scraping Page {page}...")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select(".quote")

    for quote in quotes:

        text = quote.select_one(".text").text.strip("“”")
        author = quote.select_one(".author").text

        tags = quote.select(".tag")
        tag_list = [tag.text for tag in tags]
        tag_string = ", ".join(tag_list)

        all_quotes.append({
            "Quote": text,
            "Author": author,
            "Tags": tag_string
        })

print(f"Total Quotes Scraped: {len(all_quotes)}")

with open("output_new.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["Quote", "Author", "Tags"]
    )

    writer.writeheader()

    for item in all_quotes:
        writer.writerow(item)


print("✅ Data saved to output.csv")