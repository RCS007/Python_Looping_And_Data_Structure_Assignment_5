# Question 5

# Create a dictionary of names and birthdays of Indian Prime Ministers. When you run your program it should ask
# the user to enter a name of the Prime Minister, and return the birthday.

# Date of birth : Name of Prime Minister
# 14 November 1889 : Jawaharlal Nehru
# 29 February 1896 : Morarji Desai
# 4 July 1898 : Gulzarilal Nanda
# 23 December 1902 : Charan Singh
# 2 October 1904: Lal Bahadur Shastri
# 19 November 1917 Indira Gandhi
# 4 December 1919 Inder Kumar Gujral
# 28 June 1921 P. V. Narasimha Rao
# 25 December 1924 Atal Bihari Vajpayee
# 1 July 1927 Chandra Shekhar
# 25 June 1931 Vishwanath Pratap Singh
# 26 September 1932 Manmohan Singh
# 18 May 1933 H. D. Deve Gowda
# 20 August 1944 Rajiv Gandhi
# 17 September 1950 Narendra Modi

# The interaction should look something like this:
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Jawaharlal Nehru
# Narendra Modi
# Rajiv Gandhi

# .(List all the names)
# >>> Whose birthday do you want to look up?
# Rajiv Gandhi
# >>> Rajiv Gandhi’s birthday is 20 August 1944.


# Dictionary containing the names and birthdays of Indian Prime Ministers
birthday_dict = {
    "Jawaharlal Nehru": "14 November 1889",
    "Morarji Desai": "29 February 1896",
    "Gulzarilal Nanda": "4 July 1898",
    "Charan Singh": "23 December 1902",
    "Lal Bahadur Shastri": "2 October 1904",
    "Indira Gandhi": "19 November 1917",
    "Inder Kumar Gujral": "4 December 1919",
    "P. V. Narasimha Rao": "28 June 1921",
    "Atal Bihari Vajpayee": "25 December 1924",
    "Chandra Shekhar": "1 July 1927",
    "Vishwanath Pratap Singh": "25 June 1931",
    "Manmohan Singh": "26 September 1932",
    "H. D. Deve Gowda": "18 May 1933",
    "Rajiv Gandhi": "20 August 1944",
    "Narendra Modi": "17 September 1950"
}

# Welcome message and list of names
print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthday_dict:
    print(name)

# Ask the user whose birthday they want to look up
search_name = input("\nWhose birthday do you want to look up? ")

# Check if the name exists in the dictionary
if search_name in birthday_dict:
    print(f"{search_name}'s birthday is {birthday_dict[search_name]}")
else:
    print("Sorry, we don't have that information.")
