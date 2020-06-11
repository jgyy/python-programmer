ashley_email = 'ashley@example.com'
dalton_email = 'dalton@example.com'
elizabeth_email = 'elizabeth@example.com'
# 1) Set the emails variable to be an empty dictionary
emails = {}

assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(emails)}"

# 2) Add 'ashley', 'craig', and 'elizabeth' to the emails dictionary without reassigning the variable.
emails['ashley'] = ashley_email
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = elizabeth_email

assert emails == {
    "ashley": ashley_email,
    "craig": "craig@example.com",
    "elizabeth": elizabeth_email,
}, f"Expected `emails` to be {{'ashley': '{ashley_email}', 'craig': 'craig@example.com', 'elizabeth': '{elizabeth_email}'}} but got: {repr(emails)}"

# 3) Remove 'craig' from the emails dictionary without reassigning the variable.
del emails["craig"]

assert emails == {
    "ashley": ashley_email,
    "elizabeth": elizabeth_email,
}, f"Expected `emails` to be {{'ashley': '{ashley_email}', 'elizabeth': '{elizabeth_email}'}} but got: {repr(emails)}"

# 4) Add 'dalton' to the emails dictionary without reassigning the variable.
emails["dalton"] = dalton_email

assert emails == {
    "ashley": ashley_email,
    "elizabeth": elizabeth_email,
    "dalton": dalton_email,
}, f"Expected `emails` to be {{'ashley': '{ashley_email}', 'elizabeth': '{elizabeth_email}', 'dalton': '{dalton_email}'}} but got: {repr(emails)}"

# 5) Return a list of keys from the emails dictionary as `users`
users = list(emails.keys())

assert users == [
    "ashley",
    "elizabeth",
    "dalton",
], f"Expected `users` to be ['ashley', 'elizabeth', 'dalton'] but got: {repr(users)}"

# 6) Return a list of values from the emails dictionary as `email_list`
email_list = list(emails.values())

assert email_list == [
    ashley_email,
    elizabeth_email,
    dalton_email,
], f"Expected `email_list` to be ['ashely@example.com', '{elizabeth_email}', '{dalton_email}'] but got: {repr(email_list)}"

# 7) Return a list of tuples called `pairs` representing the key/value pairs in `emails`.
pairs = list(emails.items())

assert pairs == [
    ("ashley", ashley_email),
    ("elizabeth", elizabeth_email),
    ("dalton", dalton_email),
], f"Expected `pairs` to be [('ashley', '{ashley_email}'), ('elizabeth', '{elizabeth_email}'), ('dalton', '{dalton_email}')] but got: {repr(pairs)}"
