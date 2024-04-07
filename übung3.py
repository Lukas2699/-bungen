import math

class Figur:
    def __init__(self):
        self.name = "Figur"
    
    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"

class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__()
        self.name = "Dreieck"
        self.a = a
        self.b = b
        self.c = c
    
    def Umfang(self):
        ab = math.sqrt((self.b.x - self.a.x)**2 + (self.b.y - self.a.y)**2)
        bc = math.sqrt((self.c.x - self.b.x)**2 + (self.c.y - self.b.y)**2)
        ca = math.sqrt((self.a.x - self.c.x)**2 + (self.a.y - self.c.y)**2)
        return ab + bc + ca
    
    def __str__(self):
        return f"Dreieck {self.a} - {self.b} - {self.c}"

class Rechteck(Figur):
    def __init__(self, bottom_left, top_right):
        super().__init__()
        self.name = "Rechteck"
        self.bottom_left = bottom_left
        self.top_right = top_right
    
    def Umfang(self):
        width = abs(self.top_right.x - self.bottom_left.x)
        height = abs(self.top_right.y - self.bottom_left.y)
        return 2 * (width + height)
    
    def __str__(self):
        return f"Rechteck {self.bottom_left} - {self.top_right}"

class Kreis(Figur):
    def __init__(self, center, radius):
        super().__init__()
        self.name = "Kreis"
        self.center = center
        self.radius = radius
    
    def Umfang(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Kreis M={self.center} r={self.radius}"

class Polygon(Figur):
    def __init__(self, *vertices):
        super().__init__()
        self.name = "Polygon"
        self.vertices = vertices
    
    def Umfang(self):
        perimeter = 0
        for i in range(len(self.vertices)):
            j = (i + 1) % len(self.vertices)
            perimeter += math.sqrt((self.vertices[j].x - self.vertices[i].x)**2 + 
                                   (self.vertices[j].y - self.vertices[i].y)**2)
        return perimeter
    
    def __str__(self):
        vertices_str = " - ".join([str(vertex) for vertex in self.vertices])
        return f"Polygon {vertices_str}"
