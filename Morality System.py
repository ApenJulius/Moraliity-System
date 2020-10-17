morality = 0

test = input("You see someone by a cliff, do you:\n1.Warn them about getting too close\n2.Push them off\n")
if test == "1":
    morality = morality + 1
elif test == "2":
    morality = morality - 1

test = input("A child drops its icecream, do you:\n1.Console the child\n2.Laugh and mock the child\n")
if test == "1":
    morality = morality + 1
elif test == "2":
    morality = morality - 1

test = input("You are given immunity and a gun, do you:\n1.Kill someone\n2.Not kill someone\n")
if test == "1":
    morality = morality + 1
elif test == "2":
    morality = morality - 1

test = input("You are given the cure to aids, do you:\n1.Cure aids\n2.Destroy the cure\n")
if test == "1":
    morality = morality + 1
elif test == "2":
    morality = morality - 1

if morality == -4:
    print("You absolute evil man")
elif morality == -1 or morality == -2 or morality == -3:
    print("you kinda evil man")
elif morality == 1 or morality == 2 or morality == 3:
    print("You kinda nice")
elif morality == 4:
    print("pretty nice person aint ya")
