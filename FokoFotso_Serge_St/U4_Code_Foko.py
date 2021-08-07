import math

def tilefunc(myarray, p):
    ''' Diese Funktion berechnen das Perzentile
        args: myarray: a list auf Daten
            p: ein Perzentile zu berechnen '''
    if p < 0:
        raise valueError("Negativ zahl")
    n = len(myarray)
    i = p*n
    j = int(i)
    if n==1:
         return myarray[0]
    elif (i-j)==0:
        return (myarray[j-1]+myarray[j])/2
    elif (int()+1) < n:
        return myarray[j]
    else:
        print("Es gibt kein Datei in der Array")
        return 0

def mean(data):
    if len(data) == 0:
        raise ZeroDivisionError("Leer List")
    return sum(data)/len(data)

def variance(data, probabilities=[]):
    '''Berechnen die Varianz
    args: data: list auf Daten
          probabilities: list auf Wahrscheinlichkeit der Daten'''
    m = mean(data)
    var = 0
    if len(data) == 0:
        raise ZeroDivisionError("Leer List")
    if len(probabilities)==0:
        for i in range(len(data)):
            var += (data[i]-m)**2
        return var/len(data)
    elif len(data)==len(probabilities)>0:
        for i in range(len(data)):
            var += probabilities[i]*pow((data[i] - m), 2)
        return var
    else:
        raise ValueError("Fehler in den Eingaben Werte")



def u4():
    '''zur den Aufgabe 4, berechne Varianz und Standardabweichung '''
    varianz = 0
    data = []
    try:
         with open('U4_Input_Foko.csv') as f:
            next(f)
            for line in f:
                a, b = line.split(';')
                data.append(int(b))
            #print(data)
    except:
           print("Error0")
    data.sort()
    varianz = variance(data)

    try:
          with open('U4_Output_Foko.csv', "w") as f:
             f.write(f"{'    Varianz und Standardabweichung':}\n\n")
             f.write("Varianz:  " + str(varianz) + "\n")
             f.write('Standardabweichung: ' + str(math.sqrt(varianz)))

    except:
         print("Error2")


u4()