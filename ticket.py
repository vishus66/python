age="plz enter your age and other member age"
active=True
while active:
    members=int((input(age)))
    if members=='quit':
        active=False
        continue
    elif members>3 and members<12:
        print("The ticket charges are 12$")
    elif members>12 and members<100:
        print("The ticket charge are 18$")
    elif members<3:
        print("the ticket charge is free")
    else:
        print("this type of age is invaled")
        break
