import pandas as pd

#this function return a list of all gld1 controlled genes(No threshold)
def getgld1():

    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('gld1sup1.xls')
    genelist = dataframe1["geneName"].to_list()
    genelistupper = [str(gene).upper() for gene in genelist]
    return genelistupper


getgld1()