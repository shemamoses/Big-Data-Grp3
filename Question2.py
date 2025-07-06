def check_palindrome():
    text = input("\nEnter a string to check if it's a palindrome: ")
    reversed_text = text[::-1]

    if text.lower() == reversed_text.lower():
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

# Call the function
check_palindrome()