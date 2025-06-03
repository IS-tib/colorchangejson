import pandas as pd
import json
import random

segment_color = {}
segment_ids = []

with open("fullstate.json", "r") as file:
    state = json.load(file)

def generate_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    hex_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return hex_color

for layer in state["layers"]:
    if layer.get("type") == "segmentation" and "segments" in layer:
        for segment in layer["segments"]:
            seg_id = str(segment)
            segment_ids.append(seg_id)
            segment_color[seg_id] = generate_color()
        layer["segmentColors"] = segment_color
        layer["segments"] = segment_ids
        break

with open("fullmodified.json", "w") as final:
    json.dump(state, final, indent=2)












