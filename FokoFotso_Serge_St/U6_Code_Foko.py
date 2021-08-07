def quartil(mylist, p):
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
        print("Es gibt kein Datei in der Array")
        return 0


def u6():
    '''zur den Aufgabe 6, berechne daten für Box-Plots'''
    spannweite = 0
    viertel=0
    dreiviertel=0
    interquartilsabstand=0
    data = []
    try:
         with open('U6_Input_Foko.csv') as f:
            next(f)
            for line in f:
                a, b = line.split(';')
                data.append(int(b))

    except:
           print("Error0")
    data.sort()
    viertel = quartil(data, 0.25)
    median = quartil(data, 0.5)
    dreiviertel = quartil(data, 0.75)
    interquartilsabstand = dreiviertel-viertel
    try:
          with open('U6_Output_Foko.csv', "w") as f:
             f.write(f"{' Box-Plots':^20s}\n\n")
             f.write("25%-Perzentil: " + str(viertel) + "\n")
             f.write("50%-Perzentil: " + str(median) + "\n")
             f.write("75%-Perzentil: " + str(dreiviertel) + "\n")
             f.write('IQR : '+ str(interquartilsabstand)+ "\n")
             f.write("1,5 IQR :"+ str(1.5*interquartilsabstand) +"\n")
             f.write("3.0 IQR :" + str(3.0*interquartilsabstand) )
    except:
         print("Error2")


u6()