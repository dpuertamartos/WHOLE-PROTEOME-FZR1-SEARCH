def clean_fastas_arm(gps_arm_batch_result, clean_file):
    #read the dirty text file from GPS-ARM
    with open('2_fastas.arm.txt', 'r') as f:
        lines = f.readlines()
    #create dictionary with protein ID as key, and KEN-BOX/D-BOX as a list
    last = "probando"
    hash = {"probando":[]}
    for i in range(1,len(lines)-1):
        if lines[i][0] == ">":
            last = lines[i]
        else:
            if lines[i-1][0] == ">":
                hash[last] = [lines[i]]
            else:
                hash[last].append(lines[i])

    #create the clean text
    with open('3_fastasArmCleaned.txt', 'w') as f:
        for key in hash:
            f.write(key)
            for element in hash[key]:
                f.write(element)

#clean_fastas_arm('2_fastas.arm.txt','3_fastasArmCleaned.txt')


