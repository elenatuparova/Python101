def increasing_or_decreasing(seq):
    lst = seq[1:]
    is_inc = all([lst[lst_index] > seq[lst_index] for lst_index in range(len(lst)) ])
    is_dec = all([lst[lst_index] < seq[lst_index] for lst_index in range(len(lst)) ])
    if is_inc:
        return 'Up!'
    elif is_dec:
        return 'Down!'
    return False