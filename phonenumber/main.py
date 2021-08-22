import phonenumbers
from test import myNumber

from phonenumbers import geocoder
ch_number = phonenumbers.parse(myNumber, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier

service = phonenumbers.parse(myNumber, "RO")
print(carrier.name_for_number(service, "en"))