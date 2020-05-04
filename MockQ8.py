def longest_sequence(s):
    curr_char = s[0]
    curr_count = 1
    long_char = ""
    temp = ""
    long_count = 0
    for i in range(len(s)-1):
        if curr_char == s[i+1]:
            curr_count += 1
        else:
            curr_char = s[i+1]
            curr_count = 1
        if curr_count > long_count:
            long_char = curr_char
            long_count = curr_count
    return(long_char, long_count)


assert longest_sequence("dghhhmhmx") == ("h", 3)
assert longest_sequence("dhkkhhkkkt") == ("k", 3)
assert longest_sequence("abbbadddadd") == ("b", 3)
