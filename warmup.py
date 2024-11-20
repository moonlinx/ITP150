lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def count_events(lst):
    count = 0
    # for i in list:
    #     if i % 2 == 0:
    #         count += 1
    for index in range(len(lst)):
        if lst[index] %2 == 0:
            count += 1
    return count
