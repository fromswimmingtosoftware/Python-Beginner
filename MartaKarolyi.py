import random
def podiumPlacement(placement):
    if placement == 1:
        return ("You're a winner")
    elif placement == 2:
        return ("You're the first loser")
    elif placement == 3:
        return ("At least you medaled")
    elif placement >= 4:
        return ("You will never get an international assignment")

results = random.randint(1,8)
martasReaction = podiumPlacement(results)
print(martasReaction)
