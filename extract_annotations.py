from owlready2 import *
import csv
from tqdm import tqdm

owl_file = "go.owl"
onto = get_ontology(owl_file).load()


with open('annotations.csv', 'w', newline='') as file:
    fields = ["Class", "IAO_0000115"]
    writer = csv.DictWriter(file, fieldnames = fields)
    writer.writeheader() 
    for x in tqdm(onto.classes()):
        if len(x.IAO_0000115):
            writer.writerows([{
                "Class": str(x), 
                "IAO_0000115": " ".join(x.IAO_0000115),
            }])