# Using Keyword Arguments
def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

print(contact_card("Keith", 29, "Honda Civic"))
print(contact_card(age=29, car_model="Civic", name="Keith"))
print(contact_card("Keith", car_model="Civic", age="29"))

# Defining Parameters with Default Arguments
def can_drive(age, driving_age=16):
    return age >= driving_age

print(can_drive(16))
print(can_drive(16, driving_age=18))
