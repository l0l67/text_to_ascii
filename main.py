import json
import pprint

def to_ascii(input_string):
    f = open('all.json', 'r')
    db = json.load(f)

    letter = input_string.lower()
    
    count = 0

    res = []
    let = []

    for i in letter:
        let.append(i)

    while count < 5:
        cc = 0
        for j in let:
            try:
                res.append(db['data'][j][str(count)])
            except Exception as e:
                res.append(db['data']["_"][str(count)])     #if unknown char print "_"
            print(res[cc] + " ", end="")
            cc += 1

        for j in let:
            res.pop(0)
            
        print("")
        count += 1

to_ascii(input("text: "))