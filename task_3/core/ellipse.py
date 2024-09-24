import math

from .basics import Position, GeometricPrimitive
from .utils import GeometryUtils


class Ellipse(Position, GeometricPrimitive):
    def __init__(
            self,
            x: int,
            y: int,
            major_axis: int,
            minor_axis: int,
            color: str = "black",
            visible: bool = True,
    ):
        Position.__init__(self, x=x, y=y)  # noqa dataclasses
        GeometricPrimitive.__init__(self, color=color, visible=visible)  # noqa dataclasses
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    @property
    def perimeter(self) -> float:
        h = ((self.major_axis - self.minor_axis) ** 2) / ((self.major_axis + self.minor_axis) ** 2)
        perimeter = math.pi * (self.major_axis + self.minor_axis) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
        return perimeter

    @property
    def area(self) -> float:
        return math.pi * self.major_axis * self.minor_axis / 4

    def is_within_bounds(self) -> bool:
        return GeometryUtils.is_within_bounds(self.x, self.y, self.major_axis, self.minor_axis)

    def __str__(self):
        return f"Эллипс на позиции ({self.x}, {self.y}) с осями {self.major_axis} и {self.minor_axis}\n" \
               f"Цвет: {self.color}, Видимость: {self.visible}\n" \
               f"Площадь: {self.area}, Периметр: {self.perimeter}\n" \
               f"В пределах области: {self.is_within_bounds()}\n"
