
def merge_crazy_string(left, right):
    i,j = 0, 0
    sorted_string = []
    while i < len(left) and j < len(right):
        if left[i].islower():
            if right[j].islower():
                if left[i] < right[j]:
                    sorted_string.append(left[i])
                    i = i+1
                else:
                    sorted_string.append(right[j])
                    j = j+1
            else:
                sorted_string.append(left[i])
                i = i+1

        elif left[i].isupper():
            if right[j].isupper():
                if left[i] < right[j]:
                    sorted_string.append(left[i])
                    i = i+1
                else:
                    sorted_string.append(right[j])
                    j = j+1
            elif right[j].isdigit():
                sorted_string.append(left[i])
                i = i+1 
            else:
                j = j + 1

        elif left[i].isdigit():
            if right[i].isdigit():
                if int(left[i]) < int(right[i]):
                    sorted_string.append(left[i])
                    i += 1
                else:
                    sorted_string.append(right[j])
                    j += 1
            else:
                sorted_string.append(left[i])
                i += 1

    while i < len(left):
        sorted_string.append(left[i])
        i += 1

    while j < len(right):
        sorted_string.append(right[j])
        j += 1

    return sorted_string

def sortCrazy(string:str)->str:

    if len(string) <= 1:
        return string
    
    mid = len(string) // 2
    left = sortCrazy(string[:mid])
    right = sortCrazy(string[mid:])
    return ''.join(merge_crazy_string(left, right))


