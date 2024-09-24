from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y


@dataclass
class BoundingBox:
    width: int
    height: int

    def get_bounding_box(self) -> tuple[int, int]:
        return self.width, self.height


@dataclass
class GeometricPrimitive:
    color: str = 'black'
    visible: bool = True

    def set_color(self, color: str):
        self.color = color

    def set_visibility(self, visible: bool):
        self.visible = visible

    def get_color(self) -> str:
        return self.color

    @property
    def is_visible(self) -> bool:
        return self.visible
