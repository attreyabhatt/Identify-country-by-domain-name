import json
import random

country_domain_file = open("country-by-domain-tld.json")
data = json.load(country_domain_file)
country_domain_file.close()

number_of_countries_tld = len(data)

score = 0
while True:
    random_number = random.randrange(0,number_of_countries_tld)
    country_tuple, domain_tuple = data[random_number].items()
    country_name = country_tuple[1]
    domain_name = domain_tuple[1]

    print("Domain name is: " + domain_name)
    country_name_user_input = input("Identify the country name :")
    country_name_user_input = country_name_user_input.lower()

    if country_name is not None and domain_name is not None:
        if country_name_user_input == country_name.lower():
            print("Correct")
            score = score + 1
        else:
            print("Wrong. The correct answer is: " + country_name)
            score = score - 1
        if score > 0 :
            print("Current Score: " + str(score))
        else:
            print("Current Score: 0")
        

