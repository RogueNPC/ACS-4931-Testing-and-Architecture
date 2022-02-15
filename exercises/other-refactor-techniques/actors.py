# by Kami Bigdely
# Extract class
class Actor:

    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = Email(email)

    def send_email(self):
        if self.birth_year > 1985:
            print(self.first_name, self.last_name)
            print('Movies Played: ', end='')
            for m in self.movies:
                print(m, end=', ')
            print()
            self.email.send_hiring_email()


class Email:

    def __init__(self, email):
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)

# first_names = ['elizabeth', 'Jim']
# last_names = ['debicki', 'Carrey']
# birth_year = [1990, 1962]
# movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
#      ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
# emails = ['deb@makeschool.com', 'jim@makeschool.com']

elizabeth = Actor(
    'Elizabeth', 'Debicki', 1990, 
    ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
    'deb@makeschool.com'
)

jim = Actor(
    'Jim', 'Carrey', 1962, 
    ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'],
    'jim@makeschool.com'
)

elizabeth.send_email()
jim.send_email()
    
# for i, value in enumerate(emails):
#     if birth_year[i] > 1985:
#         print(first_names[i], last_names[i])
#         print('Movies Played: ', end='')
#         for m in movies[i]:
#             print(m, end=', ')
#         print()
#         send_hiring_email(value)
