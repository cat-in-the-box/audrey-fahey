print("Are you a dog person or a cat person? Let's find out!")
activity1 = input("Do you like to spend your afternoons curled up by a window with a warm cup of tea or coffee watching the hours go by?" )
if(activity1 == "no"):
    activity2 = input("Do you like to spend your afternoons out on a hike in the woods or canoeing on the lake? Outside in general? ")
    if(activity2 == "yes"):
        print("You're a dog person!")
    else:
        print("You might be a cat person!")
else:
    print("You're a cat person!")
            