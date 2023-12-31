# Instructions to run the code

1. Run `python3 extract_annotations.py` to store the annotations in the ontology to a csv file. Make sure `owl_file` in the code has the path to the ontology.
2. Create and start a local installation of BERN2 as given [here](http://bern2.korea.ac.kr/documentation).
3. Run `python3 extract_entities.py` to extract the entities from the annotations using BERN2 and store them along with their types to entities.csv.
4. Follow based on the method:
    1. For Intersection method:
        
        Run `python3 intersection.py`.
        
    2. For Union method:
        1. Add two classes with labels "is_related_to_domain" and "is_related_to_range" to the ontology using Protege or any other tool. Make sure that owl_base in union.py has the path to this file.
        2. Run `python3 union.py`.

5. Make sure the modified ontology does not have any illegal characters.

6. Normalise the modified ontology following the steps mentioned [here](https://github.com/bio-ontology-research-group/el-embeddings).

7. Rum [EmEL++](https://github.com/kracr/EmELpp/tree/master) on the normalised ontology.