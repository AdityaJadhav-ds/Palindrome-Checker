print("🔁 Welcome to the Palindrome Checker!")

while True:
    word = input("\nEnter a word (or 'exit' to quit): ")

    if word.lower() == 'exit':
        print("👋 Goodbye!")
        break

    # Remove spaces and convert to lowercase
    cleaned = word.replace(" ", "").lower()

    if cleaned == cleaned[::-1]:
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")
