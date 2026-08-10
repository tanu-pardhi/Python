people=[1,2,3,4,5,6,7,] 
k=3
def execution (people,cur):
    if len(people)==1:
        print (people[0])
        return
    next = (cur+k-1)%len(people)
    people.pop(next)
    execution(people,next)
execution (people,0)
