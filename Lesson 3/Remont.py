L, W, H = map(int, input().split())

polePowierzchni= (((L*H)*2 + (W*H)*2))

if (polePowierzchni % 16 == 0):
    print(polePowierzchni // 16)
else:
    print(polePowierzchni // 16 + 1)

def fuv():
    print()