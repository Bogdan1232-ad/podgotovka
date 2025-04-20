N = int(input())
K = int(input())
A = int(input())
M = int(input())
T = int(input())

# Сложность первой задачи
comp_1 = A
# Сложность второй задачи
comp_2 = 2 * A
# Сложность задачи N уровня
comp_N = N * A

# Словарь для хранения количества задач по сложности
dic = {}
for i in range(1, N + 1):
    dic["N" + str(i)] = K

# Словарь для хранения времени, необходимого для решения задач по сложности
dic_for_comp = {}
for i in range(1, N + 1):
    dic_for_comp["CompEn" + str(i)] = i * A

# Если время на чтение задачи больше или равно времени до конца дня, то сразу выводим "No"
if T - M < 0:
    print('No')
else:
    # Проверяем, может ли Слава решить хотя бы одну задачу
    for i in range(1, N + 1):
        time_needed = dic_for_comp["CompEn" + str(i)]
        if time_needed + M <= T and dic["N" + str(i)] > 0:
            print("Yes")
            break
    else:
        print("No")
