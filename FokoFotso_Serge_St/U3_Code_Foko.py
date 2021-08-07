def tilefunc(mylist, p):
    ''' Diese Funktion berechnen das Perzentile
        args: mylist: a list auf Daten
            p: ein Perzentile zu berechnen '''
    if p < 0:
        raise valueError("Negativ Eingabe")
    n = len(mylist)
    i = p*n
    j = int(i)
    if n==1:
         return mylist[0]
    elif (i-j)==0:
        return (mylist[j-1]+mylist[j])/2
    elif (int()+1) < n:
        return mylist[j]
    else:
        print("Es gibt kein Datei in der list")
        return 0


def u3():
    '''zur den Aufgabe 3, berechne Spannweite und Interquartilsabstand'''
    spannweite = 0
    viertel=0
    dreiviertel=0
    interquartilsabstand=0
    data = []
    try:
         with open('U3_Input_Foko.csv') as f:
            next(f)
            for line in f:
                a, b = line.split(';')
                data.append(int(b))

    except:
           print("Error0")
    data.sort()
    spannweite = max(data) - min(data)
    viertel = tilefunc(data, 0.25)
    dreiviertel = tilefunc(data, 0.75)
    interquartilsabstand = dreiviertel-viertel
    try:
          with open('U3_Output_Foko.csv', "w") as f:
             f.write(f"{'Spannweite und Interquartilsabstand':^20s}\n\n")
             f.write("Spannweite:  ")
             f.write(str(spannweite) + "\n")
             f.write("25%-Perzentil: " + str(viertel) + "\n")
             f.write("75%-Perzentil: " + str(dreiviertel) + "\n")
             f.write('Interquartilsabstand: '+ str(interquartilsabstand))

    except:
         print("Error2")


u3()