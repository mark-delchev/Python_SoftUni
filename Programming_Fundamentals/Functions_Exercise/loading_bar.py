def loading_bar(num):
    char = ""
    x = num // 10
    if num < 100:
        print(f"{num}%", end=" ")
        print(f"[{char:%<{x}}{char:.<{10 - x}}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{char:%<{x}}]")

n = int(input())
loading_bar(n)