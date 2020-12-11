"""I copied my inpust to a text file and i opened it: with open("2.1_puzzle_set.txt") as f
I took all lines one by one: for content in f
I splited upon to space character: list_a ="15-19 k: kkkkkkkkkkkkzkkkkkkk".split(" ")
I replaced : with null :list_a[1]=list_a[1].replace(":","")
I splited first characters upon to - :list_a[0]=list_a[0].split("-")
#print(list_a[0][0],list_a[0][1])
I counted password by the given letter: counted= list_a[2].count(list_a[1])
#print(counted)
if int(list_a[0][0])<=counted<=int(list_a[0][1]):
    print("true")
sum is for to calculate the how many passwords are valid
"""
sum=0
with open("2.1_puzzle_set.txt") as f:
    for content in f:
        print(content)
        list_a = content.split(" ")
        list_a[1] = list_a[1].replace(":", "")
        list_a[0] = list_a[0].split("-")
        counted = list_a[2].count(list_a[1])
        if int(list_a[0][0]) <= counted <= int(list_a[0][1]):
            sum=sum+1
            print(str(sum)+" true")