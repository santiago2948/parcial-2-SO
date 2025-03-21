def first_fit(memory, requeriment, index):
    if requeriment<=0 or index<0 or index>=len(memory):
        return None
    continuar = True
    firstRound = True
    final = len(memory) - 1
    i=index

    while continuar:
        if i==index and not firstRound:
            continuar = False
            return None
        if memory[i][1] > requeriment:
            asignament = [memory[i][0], requeriment]
            e_modified =(memory[i][0] + requeriment ,memory[i][1] - requeriment)
            memory.pop(i)
            memory.insert(i,e_modified)
            response = [memory]
            response.append(asignament[0])
            response.append(asignament[1])
            response.append(i)
            continuar = False
            return response
        if memory[i][1] == requeriment:
            asignament = memory.pop(i)
            response = [memory]
            response.append(asignament[0])
            response.append(asignament[1])
            if i == final:
                i=0
            response.append(i)
            continuar = False
            return response
        else:
            if i==final: 
                i=0
            else: 
                i+=1
            firstRound = False

def best_fit():
    return 0

def worst_fit():
    return 0
