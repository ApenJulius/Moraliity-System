def moral(test):
    if test == "1":
        return 1
    elif test == "2":
        return -1

tests = [
    "You see someone by a cliff, do you:\n1.Warn them about getting too close\n2.Push them off\n",
    "A child drops its icecream, do you:\n1.Console the child\n2.Laugh and mock the child\n",
    "You are given immunity and a gun, do you:\n1.Kill someone\n2.Not kill someone\n",
    "You are given the cure to aids, do you:\n1.Cure aids\n2.Destroy the cure\n"
]

morality = 0
for test in tests:
    answer = input(test)
    morality += moral(answer)

if morality == -4:
    print("You absolute evil man")
elif morality == -1 or morality == -2 or morality == -3:
    print("you kinda evil man")
elif morality == 1 or morality == 2 or morality == 3:
    print("You kinda nice")
elif morality == 4:
    print("pretty nice person aint ya")
