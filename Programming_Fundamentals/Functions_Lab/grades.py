def grades(grade):
    if grade >= 5.50:
        print("Excellent")
    elif 4.50 <= grade < 5.50:
        print("Very Good")
    elif 3.50 <= grade < 4.50:
        print("Good")
    elif 3.00 <= grade < 3.50:
        print("Poor")
    elif grade < 3.00:
        print("Fail")

g = float(input())
grades(g)