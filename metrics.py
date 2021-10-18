# Group 43; Tuytte Victor; De Rijck Wout

def levenshtein_distance_recursive(str1,str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    val1 = levenshtein_distance_recursive(str1[:-1], str2) + 1
    val2 = levenshtein_distance_recursive(str1, str2[:-1]) + 1
    val3 = levenshtein_distance_recursive(str1[:-1], str2[:-1]) + (str1[-1] != str2[-1])
    return min(val1, val2, val3)

def levenshtein_distance_DP(str1,str2):
    # Create matrix, should not run into memory problems as we are working with words and they don't normally exceed 50 characters
    m = [[0 for _ in range(len(str1)+1)] for __ in range(len(str2)+1)]

    # Setup the matrix
    for i in range(len(str2)+1):
        m[i][len(str1)] = len(str2)-i

    # Setup the matrix
    for j in range(len(str1)+1):
        m[len(str2)][j] = len(str1)-j

    # Calculate distance 
    for j in range(len(str1)-1,-1,-1):
        for i in range(len(str2)-1,-1,-1):
            m[i][j] = min(m[i+1][j] + 1, m[i][j+1] + 1, m[i+1][j+1] + (str1[j] != str2[i]) ) 
    
    return m[0][0]


    
  
