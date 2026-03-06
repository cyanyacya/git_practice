string = "#" 


string_cut = string.replace(" ", "\n").replace(",", "")
print(string_cut)    

with open("listparse.txt", "x") as txt:
    txt.write(string_cut)