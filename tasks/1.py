import os

config = {}

def func(path):
    return path[path.rfind("/") + 1:].replace(".py", "").replace("_", " ", 1).replace("_", ".")


for type in os.listdir("pyrob"):
    if os.path.isfile(f"pyrob/{type}"):
        continue

    for f in os.listdir(f"pyrob/{type}"):
        path = f"tasks/pyrob/{type}/{f}"

        config[path] = func(path)

import pprint

pprint.pprint(config)

import json

print(json.dumps(config))
