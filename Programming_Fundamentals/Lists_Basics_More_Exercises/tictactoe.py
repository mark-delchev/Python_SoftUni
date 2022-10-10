line1 = list(map(int, input().split(" ")))
line2 = list(map(int, input().split(" ")))
line3 = list(map(int, input().split(" ")))

if line1 == [1, 1, 1] or line2 == [1, 1, 1] or line3 == [1, 1, 1]:
    print("First player won")

elif line1 == [2, 2, 2] or line2 == [2, 2, 2] or line3 == [2, 2, 2]:
    print("Second player won")

elif line1[0] == 1 and line2[0] == 1 and line3[0] == 1 \
    or line1[1] == 1 and line2[1] == 1 and line3[1] == 1 \
        or line1[2] == 1 and line2[2] == 1 and line3[2] == 1:
    print("First player won")

elif line1[0] == 2 and line2[0] == 2 and line3[0] == 2 \
    or line1[1] == 2 and line2[1] == 2 and line3[1] == 2 \
        or line1[2] == 2 and line2[2] == 2 and line3[2] == 2:
    print("Second player won")

elif line1[0] == 1 and line2[1] == 1 and line3[2] == 1 or \
    line3[0] == 1 and line2[1] == 1 and line1[2] == 1:
    print("First player won")

elif line1[0] == 2 and line2[1] == 2 and line3[2] == 2 or \
    line3[0] == 2 and line2[1] == 2 and line1[2]:
    print("Second player won")

else:
    print("Draw!")