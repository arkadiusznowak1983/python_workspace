def netflix(Z):
    print("netflix")
    A = []
    for i in range(0, len(Z)):
        A.append(Z[i])
        B = []
        for j in range(i+1, len(Z)):
            B.append(Z[j])
            C = []
            for k in range(j+1, len(Z)):
                C.append(Z[k])
            if A == B and A == C:
                print("A")
                print(A)
                print("B")
                print(B)
                print("C")
                print(C)
            else:
                maxLen = len(A)
                if len(B) > maxLen:
                    maxLen = len(B)
                if len(C) > maxLen:
                    maxLen = len(C)
                AA = []
                for ii in range(maxLen - len(A)):
                    AA.append(0)
                print(AA)
                BB = []
                for ii in range(maxLen - len(B)):
                    BB.append(0)
                print(BB)
                CC = []
                for ii in range(maxLen - len(C)):
                    CC.append(0)
                print(CC)
                if AA == BB and AA == CC:
                    print("A")
                    print(A)
                    print("B")
                    print(B)
                    print("C")
                    print(C)


netflix([0, 1, 0, 1, 0, 1])
print("koniec")