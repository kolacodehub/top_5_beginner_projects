name_list = [0]
phone_list = [0]
email_list = [0]


def main():
    while True:
        user_name = input('Enter a contact name to add: ')
        phone_number = int(input('Enter a contact phone number: '))
        email = int(input('Enter a contact email: '))
        print('Contact added!')
        confirm = input('Will you like to add another contact (y/n): ').lower()
        name_list.append(user_name)
        phone_list.append(phone_number)
        email_list.append(email)
        if confirm == 'y':
            continue
        else:
            break

    with open('contacts.txt', mode='w') as file:
        file.write('All contacts' + '\n')
    for i in range(1, len(name_list)):
        with open('contacts.txt', mode='a') as file:
            file.write(f'{i}. {name_list[i]} - Phone: {phone_list[i]}, Email: {email_list[i]} \n')


if __name__ == '__main__':
    main()

