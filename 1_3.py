def is_palindrome_print(word):
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

def is_palindrome_return(word):
    return word == word[::-1]

word = "level"
is_palindrome_print(word)

result = is_palindrome_return(word)
print(f"{word} is a palindrome: {result}")

