def main():
    expense_names = [0]
    amount_list = [0]
    categories = [0]
    while True:
        expense_name = input('Enter the description of the expense: ')
        amount = float(input('Enter the amount: '))
        category = input('Enter the category: ')
        exit = input('Enter y to continue or n to exit: ').lower()
        amount_list.append(amount)
        expense_names.append(expense_name)
        categories.append(category)
        total_expenses = sum(amount_list)
        if exit == 'y':
            continue
        elif exit == 'n':
            break
        else:
            break
    print("Recorded Expenses")
    with open('task.txt', mode='w') as task:
        task.write(f"Recorded Expenses \n")

    for i in range(1, len(expense_names)):
        recorded_expense = f'{i}. {expense_names[i].capitalize()} - N{amount_list[i]} - Category: {categories[i].capitalize()} \n'
        with open('task.txt', mode='a') as task:
            task.write(recorded_expense)

    with open('task.txt', mode='a') as task:
        task.write(f'Total expenses: {total_expenses:.2f} \n')
        task.write("N" + " " + str(total_expenses / 2))




if __name__ == '__main__':
    main()