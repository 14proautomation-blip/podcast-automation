import requests

def fetch_reddit_post(subreddit="AskReddit"):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        print("HTTP status:", response.status_code)
        data = response.json()
        if "data" in data and "children" in data["data"]:
            post = data["data"]["children"][0]["data"]
            return {"title": post["title"], "selftext": post.get("selftext", "")}
        else:
            return {"title": "No post found", "selftext": ""}
    except Exception as e:
        print("Error:", e)
        return {"title": "Error fetching post", "selftext": ""}

if __name__ == "__main__":
    print(fetch_reddit_post())
