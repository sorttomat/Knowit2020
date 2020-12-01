liste = list([False for i in range(100001)])

fil = open("tall.txt", "r")
alle_tall = fil.readline().split(",")

for tall in alle_tall:
    liste[int(tall)] = True

for j in range(len(liste)):
    if not liste[j]:
        print(j)
