to_do_list = []
print('''
1. Add a task
2. View tasks
3. Remove a task
4. Exit
   ''')
def main():
    while True:
        user_input = int(input('Choose an option: '))
        if user_input == 1:
            user_input2 = input('Enter a task to add: ').capitalize()
            to_do_list.append(user_input2)
            print('Task added')
        elif user_input == 2:
            if to_do_list:
                for i, task in enumerate(to_do_list, start=1):
                    print(f'{i}. {task}')
            else:
                print('Your To-do-list is empty')
        elif user_input == 3:
            remove = input('Enter a task to remove: ')
            if remove in to_do_list:
                to_do_list.remove(remove)
                print(f"Task of '{remove}' removed")
            else:
                print('Task not found')
        else:
            break


if __name__ == '__main__':
    main()
