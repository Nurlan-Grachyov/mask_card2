from typing import Any


def log(filename):
    """Декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def wrapper(func: Any) -> Any:
        def inner(*args: int, **kwargs: int) -> int:
            if len(filename) > 0:
                try:
                    result = func(*args, **kwargs)
                    log_mes = f"my_function {result}\n"
                except Exception as e:
                    result = "An error occurred during code execution"
                    log_mes = f"my_function error: {e}. Inputs: {args, kwargs} \n"
                with open(filename, mode="w+", encoding="UTF-8") as file:
                    file.write("Function started\n")
                    file.write("Function finished\n")
                    file.write(log_mes)
            else:
                try:
                    print("Function started\n")
                    result = func(*args, **kwargs)
                    print("Function finished\n")
                    log_mes = f"my_function {result}"
                    print(log_mes)
                except Exception as e:
                    print("Function finished\n")
                    result = "An error occurred during code execution"
                    log_mes = f"my_function error: {e}. Inputs: {args, kwargs}"
                    print(log_mes)
            return result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Декорируемая функция, которая перемножает два значения"""
    return x * y


if __name__ == "__main__":
    print(my_function("3", "5"))
