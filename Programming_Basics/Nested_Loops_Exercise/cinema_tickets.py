taken_seats = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0
while True:
    taken_seats = 0
    movie_name = input()
    if movie_name == "Finish":
        break
    free_seats = int(input())
    for i in range (1, free_seats + 1):
        type_of_ticket = input()
        if type_of_ticket != "End":
            taken_seats += 1
            total_tickets += 1
        if type_of_ticket == "student":
            student_tickets += 1
        if type_of_ticket == "standard":
            standard_tickets += 1
        if type_of_ticket == "kid":
            kid_tickets += 1
        elif type_of_ticket == "End":
            break
    print(f"{movie_name} - {(taken_seats / free_seats) * 100:.2f}% full.")
print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.")
