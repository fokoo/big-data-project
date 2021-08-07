def u1_1():
    '''zur den Aufgabe 1.1, berechne das Arithmetisches Mittel'''
    haeufigkeitstabelle = {}
    sum = 0
    n = 0
    arithmetisches_mittel = 0
    try:
        with open('U1_1_Input_Foko.csv') as f:
            for line in f:
               l = line.split(',')
               # print(l)
               sum += float(l[1])
               n+=1
               if float(l[1]) in haeufigkeitstabelle:
                   haeufigkeitstabelle[float(l[1])]+=1
               else:
                   haeufigkeitstabelle[float(l[1])]=1
        print('table_lenght:', n)
        print('sum:', sum)
        arithmetisches_mittel = sum/n
        print(arithmetisches_mittel)
    except:
        print("Error")
    try:
        with open('U1_1_Output_Foko.csv', "w") as f:
            f.write("Häufigkeitstabelle:  ")
            f.write(str(haeufigkeitstabelle)+"\n")
            f.write("Arithmetisches Mittel:  ")
            f.write(str(arithmetisches_mittel))
    except:
        print("Error")

u1_1()