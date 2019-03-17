import json

with open('KA.json', encoding="utf8") as json_file:
    data = json.load(json_file)

index = 0
parsed_data = []
for q in data["children"]:
    if "children" in q:
        for w in q["children"]:
            if "children" in w:
                for e in w["children"]:
                    if "children" in e:
                        for r in e["children"]:
                            if "children" in r:
                                if r['title']:
                                    total_category_duration = 0
                                    category = {'category_title': r['title'], 'video_list': []}
                                    for t in r["children"]:
                                        if t["duration"]:
                                            index += 1
                                            video = {'youtube_id': t['youtube_id'], 'title': t["title"]}
                                            total_category_duration += t["duration"]
                                            video['video_duration_seconds'] = t['duration']
                                            video['video_duration_minutes'] = t['duration']/60
                                            video['thumbnail'] = t['thumbnail_urls']['default']
                                            category['video_list'].append(video)
                                        category['category_duration_seconds'] = total_category_duration
                                        category['category_duration_minutes'] = total_category_duration/60
                                    parsed_data.append(category)

with open('parsed_data.json', 'w') as outfile:
    json.dump(parsed_data, outfile, indent=4)
