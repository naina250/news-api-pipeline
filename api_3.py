import requests
import csv

url = "https://youtube138.p.rapidapi.com/channel/videos/"

headers = {
    "x-rapidapi-key":  "your_rapidapi_key_here",
    "x-rapidapi-host": "youtube138.p.rapidapi.com",
    "Content-Type":    "application/json"
}

payload = {
  	"id": "UCJ5v_MCY6GNUBTO8-D3XoAg",
  	"filter": "videos_latest",
 	"cursor": "",
  	"hl": "en",
  	"gl": "in"
}

data = requests.post(url, headers=headers, json=payload).json()
contents = data['contents']
print(contents)

with open("youtube_data.csv", "w", newline="", encoding="utf-8") as file:
	writer = csv.DictWriter(file, fieldnames=['videoID', 'title', 'lengthSeconds', 'publishedTime', 'views', 'url'])
	writer.writeheader()
	for c in contents:
		video = c.get('video', {})
		stats = video.get('stats', {})
		writer.writerow({
			'videoID' : video.get('videoId', ''),
			'title': video.get('title', ''),
			'lengthSeconds': video.get('lengthSeconds', ''),
			'publishedTime': video.get('publishedTimeText', ''),
			'views': stats.get('views', ''),
			'url': f"https://www.youtube.com/watch?v={video.get('videoId', '')}"
		})

print(f"Done.. Saved {len(contents)} to youtube_data.csv ")