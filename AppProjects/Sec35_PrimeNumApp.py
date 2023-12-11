print("Section35, Prime Number App")
import time
running = True

while running:
    print("\n Enter 1 to determine if a specific number is prime.")
    print("\n Enter 2 to determine all prime numbers within a set range.")
    option = input("Enter your choice 1 or 2:  ")

    if option == '1':
        number = int(input("Enter a number to determine if it is prime or not:  "))
        prime_status = True
        if number == 1:
            print(number, "is NEVER A PRIME NUMBER DINGUS!")
            break
        for i in range(2, number):
            print(i)
            if number % i == 0:
                prime_status = False
                break
        if prime_status:
            print(number, "is prime!")
        else:
            print(number, "is clearly not a prime number...")
        keep_going = input('Do you want to keep going? (y/n)').lower().strip()
        if keep_going != 'y':
            running = False
    elif option == '2':
        l_bound = int(input("\nEnter a number to set the lower bound for the range:  "))
        u_bound = int(input("\nEnter a number to set the upper bound for the range:  "))
        prime_status = True        
        primes = []
        start_time = time.time()

        if l_bound <= 1:
            print(l_bound, 'IS NEVER A PRIME NUMBER DUMMY!')
        elif u_bound <= 1:
            print(u_bound, "IS NEVER A PRIME NUMBER DUMB DUMB!")
        for prime_candidate in range(l_bound, u_bound+1):
            if prime_candidate > 1:
                prime_status = True
                for i in range (2, prime_candidate):
                    if prime_candidate % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False

            if prime_status:
                primes.append(prime_candidate)
                end_time = time.time()
        delta_time = round(end_time-start_time, 4)
        print("\nThe calculations for primes took ", delta_time, 's long!')
        print("The following numbers between ",l_bound, "and ", u_bound, "are prime: ")
        input("Press enter to continue!")
        for prime in primes:
            print(prime,"\t is prime!")
        keep_going = input('Do you want to keep going? (y/n)').lower().strip()
        if keep_going != 'y':
            running = False
    else:
        print('That is not an option stupid!')
print('All done! Thank you!')