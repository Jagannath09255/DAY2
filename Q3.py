import json

json_data = '''{
    "date": "2024-08-06",
    "explanation": "This is the explanation of the astronomy picture of the day.",
    "hdurl": "http://example.com/image_hd.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Astronomy Picture of the Day",
    "url": "http://example.com/image.jpg"
}'''

data = json.loads(json_data)

print("Explanation:", data.get("explanation"))
print("Title:", data.get("title"))