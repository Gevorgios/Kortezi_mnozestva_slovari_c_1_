# def find_common_elements(t1, t2, t3):
#     common_elements = set(t1) & set(t2) & set(t3)
#     return common_elements
#
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 4, 5, 6, 7)
# tuple3 = (5, 6, 7, 8, 9)
#
# common_elements = find_common_elements(tuple1, tuple2, tuple3)
#
# if common_elements:
#     print("Общие элементы, которые есть во всех кортежах:", common_elements)
# else:
#     print("Нет общих элементов во всех кортежах.")


# 2


# def find_unique_elements(t1, t2, t3):
#     unique_elements = set(t1).symmetric_difference(set(t2)).symmetric_difference(set(t3))
#     return unique_elements
#
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 4, 5, 6, 7)
# tuple3 = (5, 6, 7, 8, 9)
#
# unique_elements = find_unique_elements(tuple1, tuple2, tuple3)
#
# if unique_elements:
#     print("Уникальные элементы для каждого кортежа:", unique_elements)
# else:
#     print("Нет уникальных элементов для каждого кортежа")


# 3


# def find_common_elements_at_same_position(t1, t2, t3):
#     common_elements = []
#     for i in range(min(len(t1), len(t2), len(t3))):
#         if t1[i] == t2[i] == t3[i]:
#             common_elements.append(t1[i])
#     return common_elements
#
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (1, 3, 3, 4, 5)
# tuple3 = (1, 2, 3, 4, 6)
#
# common_elements_at_same_position = find_common_elements_at_same_position(tuple1, tuple2, tuple3)

if common_elements_at_same_position:
    print("Элементы, которые есть в каждом кортеже и находятся на той же позиции:", common_elements_at_same_position)
else:
    print("Нет элементов, которые есть в каждом кортеже и находятся на той же позиции.")