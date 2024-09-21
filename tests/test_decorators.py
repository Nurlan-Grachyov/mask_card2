from src.decorators import log


@log(filename="mylog.txt")
def my_func(x: int, y: int) -> int:
    return x * y


@log(filename="mylog1.txt")
def my_func_1(x: int, y: int) -> int:
    return x // y


@log(filename="")
def my_func_2(x: int, y: int) -> int:
    return x // y


def test_my_func(capsys):
    my_func("2", "5")
    with open("mylog.txt", mode="r", encoding="UTF-8") as file:
        text = file.read()
        print(text)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Function started\nFunction finished\nmy_function error: can't multiply sequence by non-int of type 'str'. Inputs: (('2', '5'), {}) \n\n"
    )


def test_my_func_1(capsys):
    my_func_1(15, 5)
    with open("mylog1.txt", mode="r", encoding="UTF-8") as file:
        text = file.read()
        print(text)
    captured = capsys.readouterr()
    assert captured.out == "Function started\nFunction finished\nmy_function 3\n\n"


def test_my_func_2(capsys):
    my_func_2("15", "5")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Function started\n\nFunction finished\n\nmy_function error: unsupported operand type(s) for //: 'str' and 'str'. Inputs: (('15', '5'), {})\n"
    )
