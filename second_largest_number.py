def find_second_largest():
    n = input("Enter the value of n: ")
    if (int(n) > 10 or int(n) < 2):
        print("The value of n should be between 2 and 10")
        return
    else:
        numbers = input("Enter {} numbers separated by a space: ".format(n))
        num_list = numbers.split(" ")
        num_list = num_list[:int(n)] #slice according to the value of n 

        largest = num_list[0]
        runners_up = num_list[0]
        for i in range(len(num_list)):
            if num_list[i] > largest:
                largest = num_list[i]
        for i in range(len(num_list)):
            if(num_list[i] > runners_up) and num_list[i] != largest:
                runners_up = num_list[i]
        return runners_up    



runnners_up = find_second_largest()
print("\n")
print(runnners_up)