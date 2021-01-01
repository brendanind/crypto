file = '../../../OneDrive - Wycliffe College/14. Code Breaking/texttochange.txt'
f=open(file,"r")
lines=f.readlines()
for i in range(47):
    result=[]
    for x in lines:
        result.append(x.split(' ')[i])
        if len(result)==47:
            wholetext = ""
            for i in result:
                wholetext = str(wholetext)+str(i)
            print(wholetext)
f.close()
        
    
