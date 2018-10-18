ax = -1; ay = -3
bx = 3; by = 2
cx = 2; cy = 0
up = max(ay, by); down = min(ay, by)
left = min(ax, bx); right = max(ax, bx)
if (left < cx < right) & (down < cy < up):
    print('Yes, C is in the rectangle.')
elif not((left <= cx <= right) & (down <= cy <= up)):
    print("No, C isn't in or on the rectangle.")
else:
    print('Yes, C is on the rectangle.')
