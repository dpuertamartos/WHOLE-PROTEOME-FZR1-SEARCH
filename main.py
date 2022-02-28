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

#
# print(total[0])
# ken=[]
# for row in rows:
#     print(row)
#     if "KEN" in row["sequence.residues"]:
#         ken.append(row)
#
# print(len(ken))

# A = {"op": "=",
#      "value": "Caenorhabditis elegans"}
#
# rows = template.rows(A)
#
# for row in rows:
#     print(row["primaryIdentifier"])

#TODO: 1
#OBTAIN ALL PROTEIN SEQUENCES OF C.ELEGANS

#TODO: 2
#CONVERT THEM TO GPS-ARM MANAGEABLE DATA-STRUCTURE
#(FASTA SEQUENCE LIKE THIS)
#>PROTEIN NAME
#PROTEIN SEQUENCE
#>PROTEIN NAME 2
#PROTEIN SEQUENCE

#TODO: 3
#FILTER THEM USING GPS-ARM ALGORITHM

#TODO: 4
#LINK THE POSITIVE PROTEINS TO CDS ; template = service.get_template('protein_cds_new')

#TODO: 5
#COMPARE TO GLD-1 POSITIVE

#TODO: 5-B
#COMPARE THEM TO GERMLINE EXPRESSION
