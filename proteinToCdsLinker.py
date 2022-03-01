from intermine.webservice import Service
import pandas as pd


service = Service("http://intermine.wormbase.org/tools/wormmine/service")


query=service.new_query("Protein")
query.add_constraint("organism.species","=","elegans")
query.add_constraint("primaryIdentifier","=","CE00044")
for row in query.rows():
    print(row)


# template = service.get_template('protein_cds_new')
# print(template.constraint_dict)
# template.add_constraint("Protein.primaryIdentifier","=","CE09876")
# print(template.constraint_dict)
#
#
# rows = template.rows(
#     B = {"op": "=","path":"Protein.primaryIdentifier","value": "CE09876"}
# )
#
# print(len(rows))
# for row in rows:
#     print(row)
#
# templates = service.templates
# print(templates["protein_cds_new"])