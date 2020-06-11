# Splitting and Joining Strings
phrase = "This is a simple phrase"
words = phrase.split()
print(words)
url = 'https://example.com/users/jimmy'
user = url.split('/')[-1]
print(user)
phrase = "This is a simple phrase"
words = phrase.split()
print(", ".join(words))

# Formatting Strings with format
print("Hello, my name is {}, and I really enjoy {}. Have a nice day!".format('Keith', 'Python'))
print("Hello, my name is {0}, and I really enjoy {1}. Have a nice day! - {0}".format('Keith', 'Python'))
