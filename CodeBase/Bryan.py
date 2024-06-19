def sort_abs(clases):
   print(type(clases))
   for i in range(len(clases)):
        min_index = i
        for j in range(i+1, len(clases)):
            if clases[j] < clases[min_index]:
                min_index = j
        clases[i], clases[min_index] = clases[min_index], clases[i]
    
    return clases
#se corrigio el ejercicio


