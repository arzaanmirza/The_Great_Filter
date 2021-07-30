


def country_checker(name_of_country):


    country_list = [
    "Australia",
    "United States",
    "New Zealand",
    "India",
    "England",
    "Canada"
    ]

    if name_of_country in country_list:
        print(name_of_country)
        return True
    else:
        return False
