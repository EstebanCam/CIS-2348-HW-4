'''
Esteban Camarillo
ID:1636095
Lab: 14.13
CIS 2348
'''



num_calls = 0



def partition(user_ids, i, k):
    low = (i - 1)
    mid = (i + k) // 2
    user_ids = IDs
    pivot = user_ids[mid]
    user_ids[mid], user_ids[k] = user_ids[k], user_ids[mid]
    for j in range(i, k):
        if user_ids[j] <= pivot:
            low = low + 1
            user_ids[low], user_ids[j] = user_ids[j], user_ids[low]
    user_ids[low + 1], user_ids[k] = user_ids[k], user_ids[low + 1]
    return (low + 1)



def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i < k:
        user_ids = IDs
        pivot_index = partition(user_ids, i, k)
        quicksort(user_ids, i, pivot_index - 1)
        quicksort(user_ids, pivot_index + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()


    quicksort(user_ids, 0, len(user_ids) - 1)


    print(num_calls)


    for user_id in user_ids:
        print(user_id)

