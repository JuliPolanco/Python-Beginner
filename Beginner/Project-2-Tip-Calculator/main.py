print("***Welcome to the tip calculator***")
bill_value = input("What was the total of the bill? ")
bill_value_as_float = float(bill_value)

people = input("How many people going to share the bill? ")
people_as_float = float(people)

tip = input("What percentage of tip you want to give? ")
tip_as_float = float(tip)


pay_per_person = bill_value_as_float /people_as_float

tip_charge = (tip_as_float * pay_per_person) / 100

total_per_person = pay_per_person + tip_charge
total_person_rounded = round(total_per_person,2)
total_person_roundedto2 = "{:.2f}".format(total_person_rounded)
print(f"Each person should pay: $ {total_person_roundedto2}")
