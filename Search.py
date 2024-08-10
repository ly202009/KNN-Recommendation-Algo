import os

anime_ids = []
names = []
scores = []
genres = []
english = []
japanese = []
types = []


file_path = str(os.path.dirname(__file__))
f = open(file_path + "/anime/anime-filtered.txt", 'r', encoding="utf8").readlines()
N = len(f)-1

for i in range(0,N):
    # we need to manually split the text
    # splitting f[i] by commas with no space following it
    # example: "hello world, whats up,new line" becomes "hello world, whats up" and "new line"
    w = []
    line = f[i]
    temp = ""
    for x in range(len(line)):

        if line[x] == "," and line[x+1] != " ":
            skip = 1
            w.append(temp)
            temp = ""
            continue

        temp += str(line[x])

    anime_ids.append(str(w[0]))
    names.append(str(w[1]).upper())
    scores.append(w[2])
    genres.append(w[3])
    english.append(str(w[4]).upper())
    japanese.append(w[5])
    types.append(w[7])

while(True):
    search = str(input("What would you like to search? (Q to Quit):\n(I for ID)\n(N for Name)\n")).upper()
    if(search == "I"):
        search = str(input("What?\n")).upper()
        print(search)
        try:
            index = anime_ids.index(search)
            print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index])
        except:
            print("Not Found!")
    elif(search == "N"):
        search = str(input("What?\n")).upper()
        try:
            index = names.index(search)
            print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index])
        except:
            try:
                index = english.index(search)
                print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index])
            except:
                try:
                    index = japanese.index(search)
                    print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index])
                except:
                    print("Not Found!")
    elif(search == "Q"):
        break
    else:
        print("Not an input, try again:")
        continue
