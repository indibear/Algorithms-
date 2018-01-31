randomList = [6, 4, 12, 65, 33, 23, 7, 45, 9]

print ("Original: ", randomList)

timesLooped = 0



for j in range (0, len(randomList)):
    for item in range (0, len(randomList) -1):
        if randomList[item] > randomList[item +1]:
            temp = randomList [item+1]
            randomList[item+1] = randomList[item]
            randomList[item] = temp
            timesLooped = timesLooped +1


print ("Final Outcome: ", randomList)
print ("Pass number: ", timesLooped)
