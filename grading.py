for i in range(len(grades)):
        for j in range(grades[i]):
            if grades[i]>37 and 5*j>grades[i] and 5*j-grades[i]<3:
                grades[i]=5*j
                break
            else:
                continue
    return grades