# Kieran O'Dell (kfo7qb) & Ben Walker (baw3hg)
# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)

marbles = 0
pick = 0

def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    ans = 1
    while 2**ans <= n:
        ans += 1
    return 2**(ans-1)

print("The Game of Nim\n")
while marbles <= 0:
    marbles = int(input("The number of marbles in the pile: "))
turn_choice = input("Who will start? (p or c): ")
turn = False
if turn_choice == 'p':
    turn = True

while marbles != 0:
    print("The pile has", marbles, "marbles in it.")
    if turn:
        can_take = marbles // 2
        if can_take == 0:
            can_take += 1
        take = can_take + 1
        while (take > can_take) or (take <= 0):
            take = int(input("How many marbles do you want to take (1-" + str(can_take) + "): "))
        marbles -= take
    else:
        target = pow2(marbles)
        take = marbles - (target - 1)
        if take > marbles//2:
            take = 1
        marbles -= take
        print("The computer takes", take, "marbles.")

    turn = not turn

if turn:
    print("The player wins!")
else:
    print("The computer wins!")

