class GeometryUtils:
    MAX_WIDTH = 1000
    MAX_HEIGHT = 1000

    @staticmethod
    def is_within_bounds(x: int, y: int, width: int, height: int) -> bool:
        return (0 <= x <= GeometryUtils.MAX_WIDTH - width) and (0 <= y <= GeometryUtils.MAX_HEIGHT - height)
