str=input()
dim=[]
mx=0
for x in str:
    if x in dim:
        dim=dim[dim.index(x)+1:]
    else:
        dim.append(x)
    if len(dim)>mx:
        mx=len(dim)
print(mx)
