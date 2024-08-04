def shift_table(pattern):
    m = len(pattern)
    table = [m] * 128
    for i in range(m - 1):
        table[ord(pattern[i])] = m - 1 - i
    return table

def horspool(text, pattern):
    n, m = len(text), len(pattern)
    table = shift_table(pattern)
    i = m - 1
    
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        i += table[ord(text[i])]
    return -1

text = 'JIM_SAW_ME_IN_BARBER_SHOP'
pattern = 'BARBER'

result = horspool(text, pattern)
if result == -1:
    print("Pattern not found")
else:
    print("Pattern found at position", result)
