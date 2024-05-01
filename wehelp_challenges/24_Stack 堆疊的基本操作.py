def processStackOperations(ops):
    # (ops.split(",")).split(" ")
    empty = []
    li = ops.split(",")
    li2=[]
    for n in li:
        li2.append(n.split(" "))
    print(li2)

    for n in li2:
        if len(n)==2:
            if n[0]=="push":
                empty.append(int(n[1]))
            else:
                if len(empty) !=0:
                    empty.pop(n[1])
        else:
            if n[0]=="push":
                empty.append()
            else:
                if len(empty) !=0:
                    empty.pop()
    print(empty)



processStackOperations("pop,push 1,push -3,push 5,pop,push 10")



# test = [0,1,2]

# if test.get(3) ==None:
#     print("aa")