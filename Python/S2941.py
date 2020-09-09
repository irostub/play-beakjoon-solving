S = input()
C = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for attr in C:
    S = S.replace(attr, ".")
print(len(S))