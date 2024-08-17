import tkinter as tk
from shapely.geometry import Polygon, Point

def check_point():
    point = Point(float(entry_x.get()), float(entry_y.get()))
    is_inside = any(polygon.contains(point) for polygon in polygons)
    result_label.config(text="Inside" if is_inside else "Outside")

root = tk.Tk()
root.title("Point Checker")

label_x = tk.Label(root, text="X Coordinate:")
label_x.grid(row=0, column=0)

entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1)

label_y = tk.Label(root, text="Y Coordinate:")
label_y.grid(row=1, column=0)

entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1)

check_button = tk.Button(root, text="Check", command=check_point)
check_button.grid(row=2, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

polygons = [
    Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
    Polygon([(3, 3), (4, 3), (4.5, 4), (5, 3), (6, 3.5), (6, 4.5), (5.5, 5.5), (4.5, 5.5), (3.5, 5), (3.5, 4), (3, 3.5), (3, 3)]),
    Polygon([(6, 6), (7, 6), (7.5, 6.5), (7.5, 7), (7, 7.5), (6, 7.5), (5.5, 7), (5.5, 6.5), (6, 6), (6.5, 6), (7, 6), (6, 6)])
]

root.mainloop()
