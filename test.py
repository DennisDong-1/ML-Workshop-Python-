def mainFunction(n):
    score = 0

    n = n.lower()
    print(n)
    print(n[0])

    if n[0] == 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z':
        score += 10
    else:
        return score

print(mainFunction("aishal"))

# n = "Rishal"
# score = 0

# n = n.lower()

# if n[0] == 'r':
#     score += 10

# print(score)
