from cli.arguments import parse_args
from cli.runners import init_runners


def main():
    init_runners(parse_args())


if __name__ == '__main__':
    main()