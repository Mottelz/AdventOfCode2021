class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


class Line:
    def __init__(self, start: Point, end: Point):
        self.points = [start]
        if start.x != end.x and start.y != end.y:
            temp_x = start.x
            temp_y = start.y
            dist_x, dist_y = start.x - end.x, start.y - end.y
            while temp_y != end.y and temp_x != end.x:
                temp_x += -1 if dist_x > 0 else 1
                temp_y += -1 if dist_y > 0 else 1
                self.points.append(Point(temp_x, temp_y))

        elif start.x != end.x:
            for n in range(start.x + 1, end.x + 1):
                self.points.append(Point(n, start.y))
        elif start.y != end.y:
            for n in range(start.y + 1, end.y + 1):
                self.points.append(Point(start.x, n))

    def list(self) -> str:
        out = []
        for p in self.points:
            out.append(str(p))
        return out
