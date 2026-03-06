import csv


with open("Domination account.csv",newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)

    for row in reader:
        
        print(row[2], row[3], row[4])

