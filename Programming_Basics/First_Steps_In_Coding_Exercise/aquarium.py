length = int(input())
width = int(input())
height = int(input())
taken_space = int(input()) / 100

volume = (length * width * height) / 1000
real_volume = volume - volume * taken_space
print(real_volume)
