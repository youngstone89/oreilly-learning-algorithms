import string


def is_palindrome1(w: string):
    return w[::-1] == w


def is_palindrome2(w: string):
    while len(w) > 1:
        if w[0] != w[-1]:
            return False
        w = w[1:-1]  # remove the first and the last
    return True


# zero based index system
# exclusive last index
print('{}'.format('madam'[0:-1]))

# -1 meaning the last index
print('{}'.format('madam'[-1]))

# -2 meaning the second to the last index
print('{}'.format('madam'[-2]))

print(is_palindrome1('madam'))

print(is_palindrome1('A man, a plan, a cancal. Panama!'))

print(is_palindrome2('madam'))
