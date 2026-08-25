import requests
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Required User-Agent header
headers = {
    "User-Agent": "TrendPulse/1.0"
}



try:
    response = requests.get(
        top_stories_url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    story_ids = response.json()[:500]

    print("Top 500 story IDs fetched successfully.")

except requests.RequestException as e:
    print("Error fetching story IDs:", e)
    story_ids = []


stories = []

for story_id in story_ids:

    try:
        response = requests.get(
            item_url.format(story_id),
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        story = response.json()

        if story:
            stories.append(story)

    except requests.RequestException as e:
        print(f"Error fetching story {story_id}: {e}")
        continue
print(f"Successfully fetched {len(stories)} stories.")