import requests
from TTS.api import TTS

# ----------- FETCH REDDIT POST -----------
def fetch_reddit_post(subreddit="AskReddit"):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        data = r.json()
        post = data["data"]["children"][0]["data"]
        title = post["title"]
        body = post.get("selftext", "")
        print("Fetched Reddit post:", title)
        return title, body
    except Exception as e:
        print("Reddit fetch failed:", e)
        return "Error", ""

# ----------- GENERATE AUDIO -----------
def generate_audio(text, out_file="podcast.wav"):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text=text, file_path=out_file)
    print("Audio generated:", out_file)

# ----------- MAIN PIPELINE -----------
if __name__ == "__main__":
    title, body = fetch_reddit_post()

    final_text = title + ". " + body

    if final_text.strip() == "":
        final_text = "Hello! This is a test podcast."

    generate_audio(final_text)
