def main():
    try:
        while True:
            first_number = input('Enter the first number: ')
            if first_number.isdigit():
                while True:
                    second_number = input('Enter the second number: ')
                    if second_number.isdigit():
                        print(second_number, first_number)
                        while True:
                            operators = ['+', '-', '*', '/']
                            choose_operation = input('Enter an operator: ')
                            if choose_operation in operators:
                              if choose_operation == '+':
                                  result = float(first_number) + float(second_number)
                                  print(result)
                                  return result
                              if choose_operation == '-':
                                  result = float(first_number) - float(second_number)
                                  print(result)
                                  return result
                              if choose_operation == '*':
                                  result = float(first_number) * float(second_number)
                                  print(result)
                                  return result
                              else:
                                  result = float(first_number) / float(second_number)
                                  print(result)
                                  return result
                            else:
                                print('Enter a valid operator')
                    else:
                        print('Enter only digit from 0 - 9')
            else:
                print('Enter only digit from 0 - 9')
    except ValueError:
        print('Input a valid number')
    except ZeroDivisionError:
        print('You cant divide by 0. So, input 0 -9 as your second number')
        # main()



if __name__ == '__main__':
    main()
