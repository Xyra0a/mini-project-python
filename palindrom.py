def reverse_string(text):
    result = ""
    for char in text:
        result = char + result   # put each new character at the front
    return result


if __name__ == '__main__':
    print(reverse_string("man"))   # nam