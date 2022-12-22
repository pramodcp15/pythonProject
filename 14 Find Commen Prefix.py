

strs = ["flower", "flow", "flight", "flat"]
# strs = ["dog","racecar","car"]
prefixList = []
count = 0
for i in strs:
    prefixList.append(i[count])
    for j in strs:
        if j[count] == prefixList[count]:
            pass
        else:
            prefixList.pop()
            print(("".join(prefixList)))
            exit()
    count+= 1
