def is_anagram(first_string, second_string):

    fs_sorted = merge_sort(first_string.lower())
    ss_sorted = merge_sort(second_string.lower())

    fs_join = ''.join(fs_sorted)
    ss_join = ''.join(ss_sorted)
    if not first_string or not second_string:
        if not first_string:
            return ('', ss_join, False)
        else:
            return (fs_join, '', False)
    return (fs_join, ss_join, fs_sorted == ss_sorted)


def merge_sort(v):
    if len(v) <= 1:
        return v
    mid = len(v) // 2
    left = merge_sort(v[:mid])
    right = merge_sort(v[mid:])
    return merge(left, right)


def merge(le, ri):
    result = []
    i = j = 0
    while i < len(le) and j < len(ri):
        if le[i] <= ri[j]:
            result.append(le[i])
            i += 1
        else:
            result.append(ri[j])
            j += 1
    result.extend(le[i:])
    result.extend(ri[j:])
    return result
