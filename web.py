import requests
from bs4 import BeautifulSoup

# URL of the news website (you can change this to any reliable news site)
URL = "https://www.bbc.com/news"

# Step 1: Fetch the HTML content
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Step 2: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines
# Looking for h2 tags (BBC usually uses h2 for headlines)
headlines = []
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text:  # avoid empty strings
        headlines.append(text)

# Step 4: Save headlines to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, headline in enumerate(headlines, 1):
        f.write(f"{i}. {headline}\n")

print(f"✅ Scraped {len(headlines)} headlines and saved to headlines.txt")
