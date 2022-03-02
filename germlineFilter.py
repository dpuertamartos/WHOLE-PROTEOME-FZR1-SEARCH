# The following two lines will be needed in every python script:
from intermine.webservice import Service
from gld1filter import getgld1

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
        result.append(row["symbol"].upper())

    return result

def createTextFromHash(hash, textname):
    with open(textname, 'w') as f:
        for key in hash:
            f.write(key+"\n")
            for element in hash[key]:
                f.write(element)

# create txt with all genes expressed in germline, uncomment to make it work
# with open('germlineGenes.txt', 'w') as f:
#     for row in rows:
#         f.write(row["symbol"]+"\n")

#create hash from proteinLinkedToGene(already passed through GPS-ARM)
def createHash():
    with open('proteinLinkedToGene.txt', 'r') as f:
        lines = f.readlines()

    last = ""
    hash = {}
    for i in range(len(lines)):
        if lines[i][0] == "#":
            last = lines[i].split("#")[1].split("\n")[0]
        elif lines[i][0] != ">":
            if lines[i-1][0] == "#":
                hash[last] = [lines[i]]
            else:
                hash[last].append(lines[i])
    return hash

def filterHash(hash, filterlist):
    filteredHash = {}
    for key in hash:
        if key.upper() in filterlist:
            filteredHash[key] = hash[key]
    return filteredHash

def kenbox_filter(hash):
    filteredhash = {}
    for key in hash:
        for e in hash[key]:
            if "KEN" in e:
                filteredhash[key] = hash[key]
    return filteredhash


germgenes = germLineGenes()
gld1genes = getgld1()
hash = createHash()

filteredHash = filterHash(hash,germgenes)
germgld1filteredHash = filterHash(filteredHash,gld1genes)
kengermgld1 = kenbox_filter(germgld1filteredHash)
kengerm = kenbox_filter(filteredHash)

print("Positive GPS-ARM genes->", len(hash))
print("Positive GPS-ARM genes in germline->", len(filteredHash))
print("Positive KEN-BOX  genes in germline ->", len(kengerm))
print("Positive GPS-ARM genes in germline IP gld-1->", len(germgld1filteredHash))
print("Positive KEN-BOX  genes in germline IP gld-1->", len(kengermgld1))




