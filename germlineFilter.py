# The following two lines will be needed in every python script:
from intermine.webservice import Service

service = Service("http://intermine.wormbase.org/tools/wormmine/service")

# Return a list of genes that are expressed in a specific cell or tissue.

def germLineGenes():
    template = service.get_template('Genes_expressed_in_given_tissue')

    # You can edit the constraint values below
    # A    Gene.expressionPatterns.anatomyTerms.name

    rows = template.rows(
        A={"op": "=", "value": "germ line"}
    )
    result = []
    for row in rows:
        result.append(row["symbol"])

    return result

# create txt with all genes expressed in germline, uncomment to make it work
# with open('germlineGenes.txt', 'w') as f:
#     for row in rows:
#         f.write(row["symbol"]+"\n")

with open('proteinLinkedToGene.txt', 'r') as f:
    lines = f.readlines()
print(lines)

last = ""
hash = {}
for i in range(len(lines)):
    if lines[i][0] == "#":
        last = lines[i]
    elif lines[i][0] != ">":
        if lines[i-1][0] == "#":
            hash[last] = [lines[i]]
        else:
            hash[last].append(lines[i])

print(hash)
print(len(hash))