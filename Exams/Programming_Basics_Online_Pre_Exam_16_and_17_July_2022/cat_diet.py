fat_percentage = int(input())
protein_percentage = int(input())
carbohydrates_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())
water_percentage_real = water_percentage / 100

fat_grams = (total_calories * (fat_percentage / 100) / 9)
protein_grams = (total_calories * (protein_percentage / 100) / 4)
carbohydrates_grams = (total_calories * (carbohydrates_percentage / 100) / 4)
total_grams = fat_grams + protein_grams + carbohydrates_grams
calories_per_gram = total_calories / total_grams
calories_final = calories_per_gram - (calories_per_gram * water_percentage_real)
print(f"{calories_final:.4f}")