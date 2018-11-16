import numpy as np

gap_penalty = -7
match_penalty = -4
match_reward = 5
def globalAlign(strs):
    previousStrings = []
    closeMatrix = []
    str1 = ""
    for i in range(len(strs)-1):
        str0 = strs[i]
        str1 = strs[i+1]
        print("starting alignment")
        temp = allignInParts(str0, str1,8)
        print("fixing previous strings")
        for c in previousStrings:
            for k in reversed(temp[2]):
                c = c[:k] + '-' + c[k:]
                print(len(c))
        previousStrings.append(temp[0])
        print(len(temp[0]))
        print(len(previousStrings[0]))
        str1 = temp[1]
    previousStrings.append(str1)
    return previousStrings
def allignInParts(str1, str2, recurse):
    num1 = int(len(str1)/2)
    num2 = int(len(str2)/2)
    str11 = str1[:num1]
    str12 = str1[num1:]
    str21 = str2[:num2]
    str22 = str2[num2:]
    if(recurse > 0):
        temp1 = allignInParts(str11,str21, recurse -1)
        temp2 = allignInParts(str12,str22, recurse - 1)
        temp = []
        temp.append(str(temp1[0]) + str(temp2[0]))
        temp.append(str(temp1[1]) + str(temp2[1]))
        for i in range(len(temp2[2])):
            temp1[2].append( temp2[2][i] + num2)
        temp.append(temp1[2])
        return temp
    else:
        temp1 = twoStringAlign(str11,str21)
        temp2 = twoStringAlign(str12,str22)
        temp = []
        temp.append(str(temp1[0]) + str(temp2[0]))
        temp.append(str(temp1[1]) + str(temp2[1]))
        for i in range(len(temp2[2])):
            temp1[2].append( temp2[2][i] + num2)
        temp.append(temp1[2])
        return temp
        
def twoStringAlign( str1, str2 ):
    workstr1 = "-" + str1
    workstr2 = "-" + str2
    match_arr = np.zeros( ( len( workstr1 ), len( workstr2 ) ) )
    for index in range( len( workstr1 ) ):
        match_arr[ index ][ 0 ] = index * gap_penalty
    for index in range( len(workstr2)):
        match_arr[0][index] = index * gap_penalty
        
    for row in range( len( workstr1 ) - 1 ):
        for col in range( len( workstr2 ) - 1 ):
            possibleChoices = [( match_arr[ row ][ col + 1 ] + gap_penalty ),
                               ( match_arr[ row + 1 ][ col ] + gap_penalty ),
                               ( ( match_arr[ row ][ col ] + match_reward )
							   if
                               ( workstr1[ row + 1 ] == workstr2[ col + 1 ])
                               else( match_arr[ row ][ col ] + match_penalty
							   ))]
            match_arr[ row + 1 ][ col + 1 ] = max( possibleChoices )
    return  traceBack(match_arr, workstr1, workstr2)

def traceBack(dynamicArray, str1, str2):
    keepGoing = True
    row = len(str1) - 1
    col = len(str2) - 1
    newStr1 = ""
    newStr2 = ""
    editPlacesRow = []
    editPlacesCol = []
    while(keepGoing):
        if ((str1[row] == str2[col]) and (dynamicArray[row - 1][col - 1] == dynamicArray[row][col] - 5)) or((str1[row] != str2[col]) and (dynamicArray[row -1][col - 1] == dynamicArray[row][col] + 4)):
            newStr1 = str1[row] + newStr1
            newStr2 = str2[col] + newStr2
            row = row - 1
            col = col - 1
        elif dynamicArray[row - 1][col] == dynamicArray[row][col] + 7:
            newStr1 = str1[row] + newStr1
            newStr2 = "-" + newStr2
            editPlacesRow.append(row)
            row = row - 1
        elif dynamicArray[row][col - 1] == dynamicArray[row][col] + 7:
            newStr1 = "-" + newStr1
            newStr2 = str2[col] + newStr2
            col = col -1
        if row == 0 and col == 0:
            keepGoing = False
    ret = [newStr1, newStr2, editPlacesRow]
    return ret
    
