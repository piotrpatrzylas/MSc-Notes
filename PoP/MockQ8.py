def longest_sequence(s):
    #provide implementation

    i = s[0]
    n = 0

    while n < len(s):
        if s[n] != i: break
        n += 1

    done_until = n

    while done_until < len(s):
        cur_i = s[done_until]
        cur_n = 0
        while cur_n + done_until < len(s):
            if s[cur_n + done_until] != cur_i: break
            cur_n += 1

        done_until += cur_n
        if cur_n > n: n,i = cur_n, cur_i
        if cur_n == n and cur_i < i: i = cur_i

    return (i, n)
