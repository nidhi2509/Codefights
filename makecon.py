def makeArrayConsecutive2(statues):
    statues.sort()

    return (statues[len(statues)-1]-statues[0]+1-len(statues))
