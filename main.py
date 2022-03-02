from intermine.webservice import Service
import pandas as pd
service = Service("http://intermine.wormbase.org/tools/wormmine/service")
FILENAME = "trial.csv"
#------------------GET ALL THE C.ELEGANS PROTEINS-------------------#
template = service.get_template("species_proteins_new2")
templates = service.templates
print(templates["species_proteins_new2"])

rows = template.rows(
     A = {"op": "=", "value": "Caenorhabditis elegans"}
)
# print(rows)
#
proteins = []
for row in rows:
    a = row["Protein.primaryIdentifier"]
    b = row["Protein.length"]
    c = row["Protein.sequence.residues"]
    proteins.append([a,b,c])

#PANDA DATAFRAME CREATION
df = pd.DataFrame (proteins, columns = ['primary ID','protein length','protein sequence'])
print(df)
#CONVERT DATAFRAME TO EXCEL, COMMA SEPARATED, UNCOMMENT TO DO IT
# df.to_csv(FILENAME)

#WRITE .TXT IN FASTA, UNCOMMENT TO DO IT
# with open('fastas.txt', 'w') as f:
#     for row in rows:
#         f.write(">"+row["Protein.primaryIdentifier"]+"\n"+row["Protein.sequence.residues"]+"\n")




