def u1_2():
    '''zur den Aufgabe 1.2, berechne das Arithmetisches Mittel bei klassierten Daten'''
    arithmetisches_mittel=0
    tageInterval = []
    haeuftab = []
    try:
        with open('U1_2_Input_Foko.csv') as f:
            for line in f:
                a, b, c = line.split(';')
                tageInterval.append(int(a))
                tageInterval.append(int(b))
                haeuftab.append(float(c))
    except:
           print("Error0")

  
    for i  in range(len(haeuftab)):
           arithmetisches_mittel += 0.5*(tageInterval[2*i]+tageInterval[2*i+1])*haeuftab[i]/float(sum(haeuftab)

    try:
          with open('U1_2_Output_Foko.csv', "w") as f:
             f.write(f"{'Arithmetisches Mittel bei klassierten Daten':^20s}\n\n")
             f.write("Arithmetisches Mittel:  ")
             f.write(str(arithmetisches_mittel))
    except:
         print("Error2")

u1_2()