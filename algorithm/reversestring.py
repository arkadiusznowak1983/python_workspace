
def rev(S):
    i = len(S) - 1
    revS = ""
    while i >= 0:
        revS += S[i]
        i -= 1
    return revS

print(rev("foo bar"))