import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

print("Visiting website...")
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

print(f"Found {len(books)} books! Here they are:\n")

results = []

for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text.strip()
    results.append({"title": title, "price": price})
    print(f"Book:  {title}")
    print(f"Price: {price}")
    print("-" * 40)

print("\nSaving to file...")
with open(r"C:\Users\MC\Desktop\book_prices.txt", "w", encoding="utf-8") as f:
    for item in results:
        f.write(f"{item['title']} — {item['price']}\n")

print(f"\nDone! Saved {len(results)} books to book_prices.txt on your Desktop.")