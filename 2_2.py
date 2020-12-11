sum=0
with open("2.1_puzzle_set.txt") as f:
    for content in f:
        list_a=content.split(" ")
        list_a[1] = list_a[1].replace(":", "")
        list_a[0] = list_a[0].split("-")
        first = int(list_a[0][0]) - 1
        second = int(list_a[0][1]) - 1
        if list_a[2][first] == list_a[1]:
            if list_a[2][second] != list_a[1]:
                sum=sum+1
        elif list_a[2][second] == list_a[1]:
            if list_a[2][first] != list_a[1]:
                sum=sum+1
    print("true number is " +str(sum))