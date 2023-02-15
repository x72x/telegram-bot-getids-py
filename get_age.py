import json
from datetime import datetime

with open('ages.json') as f:
    ages = json.load(f)

ids = list(map(int, ages.keys()))
min_id = ids[0]
max_id = ids[-1]

def get_date(id):
    if id < min_id:
        return [-1, datetime.fromtimestamp(ages[str(min_id)] / 1000)]
    elif id > max_id:
        return [1, datetime.fromtimestamp(ages[str(max_id)] / 1000)]
    else:
        lid = min_id
        for i in range(len(ids)):
            if id <= ids[i]:
                uid = ids[i]
                lage = ages[str(lid)]
                uage = ages[str(uid)]
                idratio = (id - lid) / (uid - lid)
                mid_age = int((idratio * (uage - lage)) + lage)
                return [0, datetime.fromtimestamp(mid_age / 1000)]
            else:
                lid = ids[i]

def get_age(id):
    d = get_date(id)
    return [
        "older than" if d[0] < 0 else "newer than" if d[0] > 0 else "approx",
        f"{d[1].month}/{d[1].year}"
    ]