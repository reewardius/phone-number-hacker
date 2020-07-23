import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

print("\n" + "  Phone information Gathering Tool   "+"\n")

num = input('Enter Phone Number with Country Code: ')
full_num = '+' + str(num)
phone_number = phonenumbers.parse(full_num)
print("The phone number is from " +
      geocoder.description_for_number(phone_number, 'en') + " .")
print("The Telecom provider of " + str(num) + " is " + carrier.name_for_number(phone_number, 'en'))
