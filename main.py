import pandas as pd
import json
import random

segment_color = {}
segment_id = []

with open("state.json", "r") as file:
    state = json.load(file)

def generate_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    hex_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return hex_color

with open("bundle1.csv", newline='') as file1:
    data = pd.read_csv("bundle1.csv")
    for index, row in data.iterrows():
        if (row["type"] == "cell"):
            segment1 = row["nucleus_id"]
            segment_id.append(str(segment1))
            segment_color[str(segment1)] = generate_color()
            segment2 = row["soma_id"]
            segment_id.append(str(segment2))
            segment_color[str(segment2)] = generate_color()

for layer in state["layers"]:
    if layer.get("type") == "segmentation" and "segmentColors" in layer:
        layer["segmentColors"] = segment_color
        layer["segments"] = segment_id
        break

with open("modified.json", "w") as final:
    json.dump(state, final, indent=2)












