from intermine.webservice import Service

with open('fastasArmCleaned.txt', 'r') as f:
    lines = f.readlines()

last = ""
hash = {}
for i in range(len(lines)):
    if lines[i][0] == ">":
        last = lines[i]
    else:
        if lines[i-1][0] == ">":
            hash[last] = [lines[i]]
        else:
            hash[last].append(lines[i])

print(hash)
print(len(hash))

service = Service("http://intermine.wormbase.org/tools/wormmine/service")


for key in hash:
    cleanProtein = key.split("\n")[0].split(">")[1]
    print(cleanProtein)
    query=service.new_query("Protein")
    query.add_constraint("organism.species","=","elegans")
    query.add_constraint("primaryIdentifier","=",cleanProtein)
    for row in query.rows():
        gene = row["symbol"].split(",")[0]
        hash[key].insert(0,("#"+gene+"\n"))
        print(cleanProtein,":","gene","->",gene)

with open('proteinLinkedToGene.txt', 'w') as f:
    for key in hash:
        f.write(key)
        for element in hash[key]:
            f.write(element)

