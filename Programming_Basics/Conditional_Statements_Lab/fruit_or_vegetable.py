fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']
food = str(input())

if food in fruits:
    print('fruit')
elif food in vegetables:
    print('vegetable')
else:
    print('unknown')
