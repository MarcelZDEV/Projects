import sqlite3

conn = sqlite3.connect('../contactbook.db')

cursor = conn.cursor()


def add_contact(name, phone_number):
    conn.execute('''INSERT INTO book (name, phone_number) VALUES (?, ?)''', (name, phone_number))


if __name__ == '__main__':
    true = False
    while not true:
        name_user = input('Type name: ')
        phone_number_user = input('Type phone number: ')
        if len(phone_number_user) == 9:
            add_contact(name_user, phone_number_user)
            print('success')
        else:
            print('Phone number must have 9 numbers')
conn.close()
