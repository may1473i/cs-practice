# Возвращает имя участника с наибольшим результатом. 
# При равенстве — того, кто раньше в списке
def winner(names: list[str], scores: list[float]) -> str:
    resultName = names[0]
    resultScore = scores[0]

    for i in range(1, len(names)):
        score = scores[i]
        if score > resultScore:
            resultScore = score
            resultName = names[i]

    return resultName

# Возвращает средний результат, округлённый до сотых. 
# Для пустого списка — 0.0
def average(scores: list[float]) -> float:
    scoresLen = len(scores)

    if scoresLen == 0: 
        return 0.0 

    sum = 0.0

    for score in scores:
        sum += score
   
    return round(sum / scoresLen, 2)

# Возвращает имена по убыванию результата. 
# При равенстве — в исходном порядке
def ranking(names: list[str], scores: list[float]) -> list[str]:
    namesLen = len(names)
    resultNames = names.copy()
    resultScores = scores.copy()

    # Сортировка пузырьком
    for i in range(namesLen - 1):
        swapped = False
        for j in range(namesLen - 1 - i):
            if resultScores[j] < resultScores[j + 1]:
                resultNames[j], resultNames[j + 1] = resultNames[j + 1], resultNames[j]
                resultScores[j], resultScores[j + 1] = resultScores[j + 1], resultScores[j]
                swapped = True
        # Если за проход не было обменов, массив уже отсортирован
        if swapped == False:
            break

    return resultNames

# Возвращает имена тех, чей результат строго выше среднего. 
# Порядок — как в списке
def above_average(names: list[str], scores: list[float]) -> list[str]:
    return