#%% Ejercicio 1: Invierte la cadena de caracteres y cambia mayúsculas a 
#                minúsculas y viceversa.
#
#   Observación:
#   La cadena de caracteres que ingrese el usuario debe estar compuesta 
#   únicamente por letras.

def strConv(Str):
    
    outStr = ""
    
    for char in Str:
        
        if ord(char) in range(65, 91):
            outStr += chr(ord(char) + 32)
        
        elif ord(char) in range(97, 123):
            outStr += chr(ord(char) - 32)
        
        else:
            raise ValueError("Str no debe tener números o caracteres especiales.")
    
    outStr = outStr[::-1]
    
    return outStr


myStr = input("Ingrese la cadena de caracteres: ")
print("El resultado es: " + strConv(myStr))


#%% Ejercicio 2: Retorna en un diccionario el número de ocurrencias para cada 
#                caracter alfanumérico contenido en una lista.

def countOccur(Str):
    
    dic = {}
    
    for char in myStr:
        
        if char not in dic:
            dic[char] = 1
        
        else:
            dic[char] += 1
    
    return dic


myStr = list(input("Ingrese la lista de caracteres: "))
print(countOccur(myStr))

#%% Ejercicio 3: Invierte el orden de los elementos de una cadena pero los 
#                caracteres especiales (@, &, %, #, =, etc.) conservan su 
#                posición