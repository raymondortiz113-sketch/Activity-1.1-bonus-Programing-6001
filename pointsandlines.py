class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

class Lines:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def are_across(self, other_line):
        # Calculamos el determinante para evitar divisiones entre cero en líneas verticales
        dx1 = self.p2.x - self.p1.x
        dy1 = self.p2.y - self.p1.y
        dx2 = other_line.p2.x - other_line.p1.x
        dy2 = other_line.p2.y - other_line.p1.y
        
        determinant = dx1 * dy2 - dy1 * dx2
        return determinant != 0  # Si no es cero, no son paralelas y se cruzan

points = []
with open("points.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            x, y = line.strip().split()
            points.append(Point(x, y))

line1 = Lines(points[0], points[1])
line2 = Lines(points[2], points[3])

if line1.are_across(line2):
    print("Las dos líneas se cruzan entre sí.")
else:
    print("Las dos líneas son paralelas y no se cruzan.")
