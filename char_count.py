# return dictionary with charater as key and number of occurences as value
def char_count(s):
    # initializing dicionary
    count = dict()
    # iterating over string
    for c in s:
        if c in count:
            count[c] += 1
        # find the error here
    return count


if __name__ == "__main__":
    s = input()
    print(char_count(s))
