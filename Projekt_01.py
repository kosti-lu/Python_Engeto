print('''
project_1.py: the first project for Engeto Online Python Academy
author: Konstantin Lugovykh
e-mail: kosti_lu@outlook.cz
discord: kosti_lu_39515
''')
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
username = input("Please, enter your username: ")
password = input("Please, enter your password: ")
registred_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
for user in registred_users:
    if password == registred_users.get(username):
        print("-" * 40),
        print(f'''Welcome to the app, {username}
We have 3 texts to be analyzed.''')
        break
else:
    print("unregistered user, terminating the program...")
    exit()
print("-" * 40)
user_selection = input("Enter a number in the range of 1 to 3 for selecting: ")
if not user_selection.isnumeric():
    print("input containts unallowed signs, terminating the program...")
    exit()
elif int(user_selection) < 1 or int(user_selection) > 3:
    print("entered number is out of the allowed range, terminating the program...")
    exit()
else:
    print("-" * 40)
selected_text = TEXTS[int(user_selection) - 1]
word_count = len(selected_text.split())
tc_words_count = len([word for word in selected_text.split() if word.istitle()])
uc_words_count = len([word for word in selected_text.split() if word.isalpha() and word.isupper()])
lc_words_count = len([word for word in selected_text.split() if word.islower()])
number_count = len([word for word in selected_text.split() if word.isnumeric()])
sum_of_num = sum([int(number) for number in selected_text.split() if number.isnumeric()])
print(f'''There are {word_count} words in the selected text.
There are {tc_words_count} titlecase words.
There are {uc_words_count} uppercase words.
There are {lc_words_count} lowercase words.
There are {number_count} numeric strings.
The sum of all the numbers is {sum_of_num}.''')
print("-" * 40)
print("LEN|     OCCURENCES     | NR.")
print("-" * 40)
len_of_word = list()
for word in selected_text.split():
    len_of_word.append(len(word.strip(".!?,;:")))
num_length = range(1, max(len_of_word) + 1)
final_graph = dict()
for parameter in num_length:
    final_graph.update({parameter: len_of_word.count(parameter)})
for visual in final_graph.items():
    print(str(visual[0]).center(2), "|", str("*" * visual[1]).ljust(18), "|", visual[1])
print("-" * 40)
print("THANK YOU FOR USING OUR ANALYZER!".center(40))