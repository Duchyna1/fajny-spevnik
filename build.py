import os

other = ".\Ostatné"

main = open("./main.tex","w",encoding="UTF-8")
main.write("\n")
h = open("./header.txt","r",encoding = "UTF-8")
_h = h.readlines()
h.close()
main.writelines(_h)
main.write("\n")
rootDir = '.'
exclude = [".git"]
for dirName, subdirList, fileList in os.walk(rootDir):
    print(dirName)
    subdirList[:] = sorted([d for d in subdirList if d not in exclude])
    if dirName != "." and dirName != "./.git":
        main.write("\\section{" + dirName[3:] + "}\n")
        if dirName == other:
            main.write("\\setleadsheets{title-template = other}\n")
        for song in sorted(fileList):
            if ".tex" in song: main.write("\t\\input{./" + dirName[2:]+"/"+song + "}\n")
        main.write("\n")
main.write("\\end{multicols}\n")
main.write("\\end{document}\n")
main.close()
