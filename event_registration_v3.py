
from datetime import datetime

first_name = input("Enter first name: ").strip().title()
last_name = input("Enter last name: ").strip().title()
section = input("Enter section: ").strip().upper()
event = input("Enter event name: ").strip().title()

year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

full_name = first_name + " " + last_name
name_code = full_name.upper()

event_date = datetime(year, month, day)

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", section)
print("Event:", event)
print("Event Date:", event_date.strftime("%B %d, %Y"))
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")

print("\nRegistration record created successfully.")