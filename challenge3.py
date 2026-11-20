user_input = input("Enter a string: ")

left, right = 0, len(user_input) - 1

while left < right:
    if user_input[left] != user_input[right]:
        print(f"The string '{user_input}' is not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print(f"The string '{user_input}' is a palindrome.")
