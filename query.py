from intermine.webservice import Service
import pandas as pd
service = Service("http://intermine.wormbase.org/tools/wormmine/service")
query=service.new_query()
query.select("Gene.symbol","Gene.primaryIdentifier", "Gene.length")
for row in query.rows(start=0,size=10):
    print(row)