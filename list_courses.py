from setup import get_canvas


def main():
    canvas = get_canvas()
    courses = canvas.get_courses()
    for i in courses:
        print(i)


if __name__ == '__main__':
    main()