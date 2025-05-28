import requests
from bs4 import BeautifulSoup

def get_hackernews_headlines():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.select(".titleline > a")

    print("\nTop Hacker News Headlines:\n")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines[:10], 1):
            title = headline.text.strip()
            link = headline.get("href")

            output = f"{i}. {title}\n   Link: {link}\n"
            print(output)
            file.write(output + "\n")

    print("\n✅ Headlines saved to 'headlines.txt'.")

if __name__ == "__main__":
    get_hackernews_headlines()
