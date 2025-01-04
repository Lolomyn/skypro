from src.decorators import log


def test_log_console_correct_input(capsys):
    @log(filename="")
    def func1(x, y):
        return x + y

    func1(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "func1 ok\n"


def test_log_console_invalid_input(capsys):
    @log(filename="")
    def func2(x, y):
        return x + y

    func2(1, "2")

    captured = capsys.readouterr()
    assert captured.out == "func2 error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"


def test_log_console_no_args(capsys):
    @log(filename="")
    def func3(x, y):
        return x + y

    func3()

    captured = capsys.readouterr()
    assert (
        captured.out == "func3 error: test_log_console_no_args.<locals>.func3() missing 2 required positional "
        "arguments: 'x' and 'y'. Inputs: (), {}\n"
    )


def test_log_file_no_args():
    @log(filename="mylog.txt")
    def func4(x, y):
        return x + y

    func4()

    with open("mylog.txt") as file:
        last_line = file.readlines()[-1].strip()
    assert (
        last_line == "func4 error: test_log_file_no_args.<locals>.func4() missing 2 required "
        "positional arguments: 'x' and 'y'. Inputs: (), {}"
    )


def test_log_file_invalid_input():
    @log(filename="mylog.txt")
    def func5(x, y):
        return x + y

    func5(1, "2")

    with open("mylog.txt") as file:
        last_line = file.readlines()[-1].strip()
    assert last_line == "func5 error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}"


def test_log_file_correct_input():
    @log(filename="mylog.txt")
    def func6(x, y):
        return x + y

    func6(1, 2)

    with open("mylog.txt") as file:
        last_line = file.readlines()[-1].strip()
    assert last_line == "func6 ok"
