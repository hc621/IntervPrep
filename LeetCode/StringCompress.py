chars = ["a","a","b","b","c","c","c"]
#chars = ["a"]
chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","b","b","a","a","a"]

anchor = write = 0
for read, c in enumerate(chars):
    if read + 1 == len(chars) or chars[read + 1] != c:
        chars[write] = chars[anchor]
        write += 1
        if read > anchor:
            for digit in str(read - anchor + 1):
                chars[write] = digit
                write += 1
        anchor = read + 1


print(chars)