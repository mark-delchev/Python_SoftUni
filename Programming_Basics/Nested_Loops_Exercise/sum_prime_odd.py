NotPrime = False
prime_sum = 0
non_prime_sum = 0
while True:
    num = input()
    if num == "stop":
        print(f"Sum of all prime numbers is: {prime_sum}")
        print(f"Sum of all non prime numbers is: {non_prime_sum}")
        break
    if num != "stop":
        num = int(num)
    if num < 0:
        print("Number is negative.")
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                NotPrime = True
                break
            else:
                NotPrime = False
    if NotPrime and num > 1:
        non_prime_sum += num
    elif not NotPrime and num > 1:
        prime_sum += num




