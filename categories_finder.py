import json
from random import shuffle

with open('data/parsed_data.json', encoding="utf8",) as json_file:
    data = json.load(json_file)

print(json.dumps(data[0]['category_duration_seconds'], indent = 4))


def get_videos_for_duration(duration):
    final_categories = []
    shuffle(data)
    total_current_duration = 0
    current_best_match_difference = duration
    last_element = {}
    for category in data:
        if 'category_duration_seconds' not in category:
            print(category)
        seconds = category['category_duration_seconds']
        if total_current_duration + seconds < duration:
            final_categories.append(category)
            total_current_duration += seconds
        elif total_current_duration + seconds == duration:
            final_categories.append(category)
            return final_categories
        else:
            if total_current_duration + seconds - duration < current_best_match_difference:
                last_element = category
                current_best_match_difference = total_current_duration + seconds - duration
    final_categories.append(last_element)

    return final_categories, current_best_match_difference


x, y = get_videos_for_duration(12000)

print('ONLY OFF BY ' + str(y)),

print(json.dumps(x, indent=4))




