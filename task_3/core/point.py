from .basics import Position, GeometricPrimitive


class Point(Position, GeometricPrimitive):
    def __init__(
            self,
            x: int,
            y: int,
            color: str = "black",
            visible: bool = True
    ):
        Position.__init__(self, x=x, y=y)  # noqa dataclasses
        GeometricPrimitive.__init__(self, color=color, visible=visible)  # noqa dataclasses

    def __str__(self):
        return f"Точка на позиции ({self.x}, {self.y}) с цветом {self.color} и видимостью {self.visible}"
