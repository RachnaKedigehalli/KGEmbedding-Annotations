import pandas as pd
from tqdm import tqdm
import requests

# Start BERN2 server
def query_plain(text, url="http://localhost:8888/plain"):
    return requests.post(url, json={'text': text}).json()

df = pd.read_csv("annotations.csv")
output_df = pd.DataFrame({"class": [], "identified_entity": [], "entity_type": []})

for i in tqdm(df.index):
    row = df.loc[i]
    x = row["IAO_0000115"]

    for ann in query_plain(x)['annotations']:
        output_df = pd.concat([output_df, pd.DataFrame({"class": [row["Class"]], "identified_entity": [ann['mention']], "entity_type": [ann['obj']]})], ignore_index = True)

print(output_df)

output_df.to_csv("entities.csv")