import json
import random

f = open("country-by-domain-tld.json")
data = json.load(f)
f.close()

number_of_countries_tld = len(data)

while True:
    random_number = random.randrange(0,number_of_countries_tld)
    country_tuple, domain_tuple = data[random_number].items()
    country_name = country_tuple[1].lower()
    domain_name = domain_tuple[1]

    print("Domain name is: " + domain_name)
    country_name_user_input = input("Identify the country name :")
    country_name_user_input = country_name_user_input.lower()

    if country_name is not None and domain_name is not None:
        if country_name_user_input == country_name:
            print("Correct")
        else:
            print("Wrong. The correct answer is: " + country_name)


