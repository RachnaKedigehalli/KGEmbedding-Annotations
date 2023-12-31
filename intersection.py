from owlready2 import *
import csv
import types
from tqdm import tqdm
import pandas as pd

class OntologyER:
    def __init__(self, onto) -> None:
        self.label_class_mapping = {}
        self.id_class_mapping = {}
        self.onto = onto
        for x in tqdm(self.onto.classes()):
            try:
                if x.label:
                    self.label_class_mapping[x.label[0]] = x
                    self.id_class_mapping[str(x)] = x
            except:
                print(x, x.label)

    def get_class_by_label(self, label):
        if label in self.label_class_mapping:
            return self.label_class_mapping[label]
        return None
    
    def get_class_by_id(self, id):
        return self.id_class_mapping[id]

    def add_relation(self, owl_class_id, new_label, category):
        with self.onto:
            class is_related_to(ObjectProperty):
                domain = [self.get_class_by_id(owl_class_id)]
                new_label_class = self.get_class_by_label(new_label)
                if not new_label_class:
                    # class with label does not exist
                    category_class = self.get_class_by_label(category)
                    if not category_class:
                        # class with category does not exist, create category
                        category_class = types.new_class(category, (Thing,))
                        self.label_class_mapping[category] = category_class
                        self.id_class_mapping[str(category_class)] = category_class
                    
                    # add new class with "new_label" as subclass to category class
                    new_label_class = types.new_class(new_label, (category_class,))
                    self.label_class_mapping[new_label] = new_label_class
                    self.id_class_mapping[str(new_label_class)] = new_label_class
                range = [new_label_class]
                    
    def get_updated_onto(self):
        return self.onto

owl_base = "go.owl"
onto = get_ontology(owl_base).load()

er = OntologyER(onto)

entity_df = pd.read_csv("entities.csv")

for entity in tqdm(entity_df.iterrows()):
    er.add_relation(owl_class_id=entity[1]["class"], new_label=entity[1]["identified_entity"], category=entity[1]["entity_type"])

er.get_updated_onto().save("modified_intersection.owl")