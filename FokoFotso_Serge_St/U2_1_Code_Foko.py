def tilefunc(myarray, p):
    ''' Diese Funktion berechnen das Perzentile
          args: myarray: a list auf Daten
              p: ein Perzentile zu berechnen '''
    n = len(myarray)
    i = p*n
    j = int(i)
    if n==1:
         return myarray[0]
    elif (i-j)==0 and i>0:
        return (myarray[int(i-1)]+myarray[int(i)])/2
    elif (int()+1) < n:
        return myarray[j]
    else:
        print("Es gibt kein Daten in der list")
        return 0


def u2_1():
    '''zur den Aufgabe 2, berechne Median und Quartile'''
    median=0
    viertel=0
    dreiviertel=0
    data = []
    try:
        with open('U2_1_Input_Foko.csv') as f:
            next(f)
            for line in f:
                a, b = line.split(';')
                for i in range(int(b)):
                    data.append(int(a))
           
    except:
           print("Error0")
    median = tilefunc(data, 0.5)
    viertel = tilefunc(data, 0.25)
    dreiviertel = tilefunc(data, 0.75)
    try:
          with open('U2_1_Output_Foko.csv', "w") as f:
             f.write(f"{'Median und Quartile':^20s}\n\n")
             f.write("Median:  ")
             f.write(str(median)+ "\n")
             f.write("25%-Perzentil: " + str(viertel) + "\n")
             f.write("75%-Perzentil: " + str(dreiviertel) + "\n")
    except:
         print("Error2")


u2_1()