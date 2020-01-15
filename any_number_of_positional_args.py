import typing


# notice that args is typed just as Any despite it being a container
# this is what you are supposed to do according to PEP 484
# https://www.python.org/dev/peps/pep-0484/#arbitrary-argument-lists-and-default-argument-values

def print_args(*args: typing.Any) -> None:
    for index, arg in enumerate(args):
        print(f"arg {index} is {arg}")
    print()


def fun_with_name_pos_args(a: typing.Any, b: typing.Any, *args: typing.Any) -> None:
    print(f"a = {a}")
    print(f"b = {b}")
    # if you want to pass an iterable to a function that takes any number of arguments
    # just put a * in front of that argument
    print_args(*args)


def fun_with_optional_args_BEFORE_star_args(a: typing.Any = 5, b: typing.Any = 20, *args: typing.Any):
    fun_with_name_pos_args(a, b, *args)


def fun_with_optional_args_AFTER_star_args(*args: typing.Any, a: typing.Any = 5, b: typing.Any = 20):
    fun_with_name_pos_args(a, b, *args)

T = typing.TypeVar('T')
def my_min(*args: T) -> T:
    cur_min = args[0]
    for val in args[1:]:
        if val < cur_min:
            cur_min = val
    return cur_min


if __name__ == '__main__':
    vals = [21, 12, 23, 14]

    print_args('hello', 'there', 3, 4)
    print_args(*vals)
    print_args(1, 2, 3, *vals)

    fun_with_optional_args_BEFORE_star_args(34, 20, 7, 8, 9)
    fun_with_optional_args_AFTER_star_args(25, 59, 89)
    fun_with_optional_args_AFTER_star_args(1, 2, 3, a=30, b=40)
    fun_with_optional_args_AFTER_star_args(10, 11, 12)

    print(f"The min of 45, 23, 87, 9 is {my_min(45, 23, 87, 9)}", end='\n' * 2)
    print(f"The min of {vals} is {my_min(*vals)}")
