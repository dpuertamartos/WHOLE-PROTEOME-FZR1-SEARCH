# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("http://intermine.wormbase.org/tools/wormmine/service")

# Return a list of genes that are expressed in a specific cell or tissue.

template = service.get_template('Genes_expressed_in_given_tissue')

# You can edit the constraint values below
# A    Gene.expressionPatterns.anatomyTerms.name

rows = template.rows(
    A = {"op": "=", "value": "germ line"}
)

for row in rows:
    print(row["symbol"], row["secondaryIdentifier"], row["expressionPatterns.primaryIdentifier"], \
          row["expressionPatterns.anatomyTerms.name"], row["expressionPatterns.anatomyTerms.synonym"])

#create txt with all genes expressed in germline, uncomment to make it work
# with open('germlineGenes.txt', 'w') as f:
#     for row in rows:
#         f.write(row["symbol"]+"\n")