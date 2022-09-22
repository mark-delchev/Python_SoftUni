number_of_people = int(input())
capacity = int(input())
number_of_evlevations_needed = number_of_people // capacity
if number_of_people % capacity != 0:
    number_of_evlevations_needed += 1
print(number_of_evlevations_needed)
