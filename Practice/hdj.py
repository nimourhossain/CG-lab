import matplotlib.pyplot as plt

def MID(x1,y1,x2,y2):
    x, y =x1,y1
    dx=x2-x1
    dy=y2-y1
    x_points=[]
    y_points=[]
    p=dy-(dx/2)
    while x<=x2:
        x_points.append(round(x))  # Round to nearest pixel``
        y_points.append(round(y))
        if(p<0):
            p+=dy
        else:
            y += 1
            p+=dy-dx

        x+=1

    return x_points,y_points
           




x1, y1 = 1, 1
x2, y2 = 5, 4
x_points , y_points = MID(x1,y1,x2,y2)


plt.plot(x_points,y_points,marker='o',color='blue')
plt.title("DDA")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()