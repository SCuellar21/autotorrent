from tpb import TPB
from constants import CATEGORIES, ORDERS
import os
import re
numbers = re.compile('\d+(?:\.\d+)?')

#Color and reset codes, to make things pretty
#Actually this doesn't work on Windows properly so fuck it
CSI = ''
RES = ''

#Some stuff that isnt really used
import webbrowser
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

def ripandprint(s):
    for i in s:
        if i.category == "Audio":
            sr.append([i.title.replace("–", "-"),float(numbers.findall(i.size)[0]),i.seeders,i.leechers,i.magnet_link,i.torrent_link])
            ct = 1
            sr.sort(key=lambda sr: sr[2])
            sr.reverse()

    if sr != []:
        print(CSI,"----------------------------------------------------------------",RES)

        for i in sr:
            print(CSI,ct,"<",i[1],"[ S:",RES,i[2],CSI," L:",RES,i[3],CSI,"]>",RES,i[0],CSI)
            ct += 1

        print(CSI,"----------------------------------------------------------------",RES)
    else:
        print(CSI,"----------------------------------------------------------------",RES)
        print("     No results found.")
        print(CSI,"----------------------------------------------------------------",RES)
    return sr


def read_file(filename):
    #open the file
    f = open(filename)

    #make a new empty list and fill it with the file's contents
    raw = []
    for line in f:
        raw.append(line)
    #make a new empty list and split it up into individual entries
    formatted = []
    for i in raw :
        formatted.append(i.split(",\""))

    ##for j in range(0,len(formatted)):
    ##    for i in range(0,3):
    ##        formatted[j][i] = formatted[j][i].replace("\"","").replace("\n","")


    formatted.pop(0)
    rt = []
    rt2 = []

    for i in formatted:
        rt.append([i[2].replace("\"",""),i[1].replace("\"","")])
    for i in rt:
        if not(i in rt2):
            rt2.append(i)

    return rt






t = TPB('https://thepiratebay.se')
print("----- MENU -----")
print("1: Search for Album")
print("2. Import CSV list")
menu = input('? ')
if menu == '1':
    searching = 1
    magnets = []
    while searching == 1 :
        search = input('Search for? ')
        s = t.search(search)
        sr = []


        #Rip torrent data
        for i in s:
            if i.category == "Audio":
                sr.append([i.title.replace("–", "-"),float(numbers.findall(i.size)[0]),i.seeders,i.leechers,i.magnet_link,i.torrent_link])
                ct = 1
                sr.sort(key=lambda sr: sr[2])
                sr.reverse()

        if sr != []:
            print(CSI,"----------------------------------------------------------------",RES)

            for i in sr:
                print(CSI,ct,"<",i[1],"[ S:",RES,i[2],CSI," L:",RES,i[3],CSI,"]>",RES,i[0],CSI)
                ct += 1

            print(CSI,"----------------------------------------------------------------",RES)


            print("Type a number to add to list of magnet links.")
            print(CSI,"q: save and quit, r: redo search",RES)
            item = input('? ')
            if item == 'r':
                print("")
            elif item == 'q':
                searching = 0
            else:
                magnets.append([sr[int(item) - 1][4],sr[int(item) - 1][0]])
                item = input('Continue searching (y/n)? ')
            if item == 'n' or item == 'N' :
                searching = 0
        else:
            print(CSI,"----------------------------------------------------------------",RES)
            print("     No results found.")
            print(CSI,"----------------------------------------------------------------",RES)

        ##Unimplemented function to launch Transmission with magnt link.
        ##os.system("open /Applications/Transmission.app %s" % sr[int(item) - 1][4])

    #end of while loop
    for i in magnets:
        print(CSI,i[1],RES)
        print(i[0],"\n")

else:
    playlist = read_file("playlist.csv")
    magnets = []
    searching = 1

    #Sort and remove duplicates
    playlist.sort()
    sortedpl = []
    for i in range(0,len(playlist)-1):
        if playlist[i][0] != playlist[i+1][0]:
            sortedpl.append(playlist[i])
    sortedpl.append(playlist[len(playlist)-1])
    playlist = sortedpl

    for i in playlist:
        print(CSI,i[0]," : ",RES,i[1])

    for album in playlist:
        #break if user decides to quit
        if searching == 4: break

        while searching != 0 :
            print("\n\n")
            #Search for stuff
            if searching == 1:
                print("Searching for: " + album[0] + " by " + album[1])
                s = t.search(album[0])
            elif searching == 2:
                print("Searching for: " + album[0] + " by " + album[1])
                s = t.search(album[1])
            else:
                search = input('Search for? ')
                s = t.search(search)

            #fetch and print
            sr = []
            sr = ripandprint(s)
            if sr != []:
                print("Type a number to add to list of magnet links.")
            else:
                print("Nothing found, you can search by artist or manually for better results.")
            print(CSI,"s: skip, a: search by artist, m: manual mode, q: save and quit",RES)

            item = input('? ')
            if item == 's':
                searching = 1
                break
            elif item == 'a':
                searching = 2
            elif item == 'm':
                searching = 3
            elif item == 'q' :
                searching = 4
                break
            else:
                magnets.append([sr[int(item) - 1][4],sr[int(item) - 1][0]])
                searching = 1
                break


    for i in magnets:
        print(CSI,i[1],RES)
        print(i[0],"\n")
