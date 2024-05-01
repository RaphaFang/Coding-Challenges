def processQueueOperations(ops):
    empty = []
    li = ops.split(",")
    li2=[]
    for n in li:
        li2.append(n.split(" "))

    for n in li2:
        if len(n)==2:
            if n[0]=="enq":
                empty.append(int(n[1]))
            else:
                if len(empty) !=0:
                    # empty.pop(n[1])
                    del empty[0]

        else:
            if n[0]=="enq":
                empty.append()
            else:
                if len(empty) !=0:
                    # empty.pop()
                    del empty[0]

    return(empty)

test = [0,1,2,3]
test.insert(0,10)
print(test)