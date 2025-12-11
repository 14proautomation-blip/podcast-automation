import requests

def fetch_reddit_post(subreddit="AskReddit"):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit=1"
    headers = {"User-agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    data = response.json()

    post = data["data"]["children"][0]["data"]
    return {
        "title": post["title"],
        "selftext": post.get("selftext", "")
    }

if __name__ == "__main__":
    print(fetch_reddit_post())
