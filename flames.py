print("Welcome to flames created by Yashodha Ajaykumar using python")
print("check the relationship status between you and your crush right now!!")
user=input("Type 'play' to play FLAMES, 'end',to exit: ")
is_on=True
if user=='play':
    per1=input("enter your name: ")
    per2=input("enter your crush name: ")
    dict={}
    for i in per1:
        if i not in dict:
            dict[i]=1
        elif i in dict:
            if dict[i]==1:
                dict[i]-=1
            else:
                dict[i]+=1
    for j in per2:
        if j not in dict:
            dict[j] = 1
        elif j in dict:
            if dict[j] == 1:
                dict[j] -= 1
            else:
                dict[j] += 1
    num=0
    for letters in dict:
        if dict[letters]==1:
            num+=1
    res=["Its F.. you are born to be friends","Its L.. you are made for each other","its A.. Affection is holding you together","Its M.. time to be thinking of family planning","Its E.., oh oh!! unluckily you both are enemies", "Its S.. sorry for informing you that u both are siblings"]
    while len(res)>1:
        split_index=(num% len(res)-1)
        if split_index>=0:
            right=res[split_index+1:]
            left=res[:split_index]
            res=right+left
        else:
            res=res[: len(res)-1]
    print(res[0])
    is_on=False
elif user=='end':
    print("thank you ")
    is_on=False
else:
    print("invalid input!!")
    is_on=False


