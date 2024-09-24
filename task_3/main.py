from core import Ellipse, Point


def main():
    ellipse = Ellipse(100, 150, 200, 100, "blue", True)
    print(ellipse)

    point = Point(50, 50, "red", True)
    print(point)


if __name__ == '__main__':
    main()
