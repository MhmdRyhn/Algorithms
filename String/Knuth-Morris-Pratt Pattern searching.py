#*** Visit following links to get more clear
# https://www.youtube.com/watch?v=v82y5TCcBhQ
# https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/



# *** failure function to generate PREFIX TABLE ***#
def failureFunction(pattern):
    pat_len = len(pattern)
    prefix_table = [0 for i in range(pat_len)]

    i, j = 1, 0

    while i < pat_len:
        if pattern[i] == pattern[j]: # if character matches with prefix
            prefix_table[i] = j + 1
            i += 1
            j += 1
        else: # if character doesn't match with prefix
            if j == 0: # if no matching before
                i += 1
            else: #if some characters matched before
                j = prefix_table[j - 1]

    return prefix_table
# *************** End failure function ***********#



# ******************* Main KMP *********************#
def KMP(pattern, text):
    positions = []

    pat_len = len(pattern)
    txt_len = len(text)

    prefix_table = failureFunction(pattern)

    i ,j = 0, 0

    while i < txt_len:
        if text[i] == pattern[j]: # if matching found, then proceed next
            i += 1
            j += 1

        if j == pat_len: # if all charcters of patter match
            positions.append(i - j)
            j = prefix_table[j - 1]
        elif i < txt_len and text[i] != pattern[j]:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return positions
# ***************** End KMP ************************#

# t='ABABDABACDABABCABABCABABAA'
# p='ABABCABAB'

t = input()
p = input()

pos = KMP(p,t)
print(*pos)
