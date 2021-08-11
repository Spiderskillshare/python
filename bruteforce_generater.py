def rite(lists):
    bets.write(lists)


alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
firs = open("wordlist.txt", "w")
firs.write("written by cyber spider \n")
firs.close()
bets = open("wordlist.txt", "a")
for word in alpha:
    for subword in alpha:
        for subsubword in alpha:
            for subsubsubword in alpha:
                for subsubsubsubword in alpha:
                    (rite(word + subword + subsubword + subsubsubword + subsubsubsubword +"\n"))
'''see = open("wordlist.txt", "r")
print(see.read())
see.close()'''
bets.close()
