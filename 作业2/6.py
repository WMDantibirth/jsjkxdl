ax = -1; ay = -3
bx = 3; by = -3
cx = 1; cy = 1
dx = 2; dy = -3
p = ((cy - ay)*(dx - ax)+ay)/(cx - ax)
q = ((cy - by)*(dx - bx)+by)/(cx - bx)
if cy > ay:
    if (p > dy) & (q > dy) & (ay < dy) & (min(ax, bx) < dx < max(ax, bx)):
        print("Yes, D is in the triangle.")
    elif (p < dy) | (q < dy) | (min(ax, bx) > dx) | (dx > max(ax, bx)):
        print("No, D is not in the triangle.")
    else:
        print("Yes, D is on the triangle.")
elif cy == ay:
    print('Wrong, have no triangle!')
else:
    if (p < dy) & (q < dy) & (ay > dy) & (min(ax, bx) < dx < max(ax, bx)):
        print("Yes, D is in the triangle.")
    elif (p > dy) | (q > dy) | (min(ax, bx) > dx) | (dx > max(ax, bx)):
        print("No, D is not in the triangle.")
    else:
        print("Yes, D is on the triangle.")
