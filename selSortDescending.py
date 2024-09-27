def select(seq, start):
    maxIndex = start
    for j in range(start + 1, len(seq)):
        if seq[j] > seq[maxIndex]:
            maxIndex = j
    return maxIndex


def selection_sort(seq):
    for i in range(len(seq) - 1):
        maxIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[maxIndex]
        seq[maxIndex] = tmp


def average_evens(seq):
    evens = [num for num in seq if num % 2 == 0]
    if len(evens) == 0:
        return None
    avg = sum(evens) / len(evens)
    return avg


if __name__ == "__main__":
    list = [2, 5, 3, 1, 4, 7, 6]
    print("Given list is")
    print(list)
    selection_sort(list)
    print("\nSorted list in descending order:")
    print(list)
    average = average_evens(list)
    print("\nAverage of even elements:")
    print(average)
