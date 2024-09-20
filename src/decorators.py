from typing import Any


def log(filename: str):
    def wrapper(func: Any) -> Any:
        def inner(*args: int, **kwargs: int) -> int:
            if filename:
                try:
                    result = func(*args, **kwargs)
                    log_mes = f"my_function {result}\n"
                except Exception as e:
                    result = 'An error occurred during code execution'
                    log_mes = f"my_function error: {e}. Inputs: {args, kwargs} \n"
                with open(filename, mode="a", encoding="UTF-8") as file:
                    file.write(log_mes)
            else:
                try:
                    result = func(*args, **kwargs)
                    log_mes = "my_function ok\n"
                    print(log_mes)
                except Exception as e:
                    result = 'An error occurred during code execution'
                    log_mes = f"my_function error: {e}. Inputs: {args, kwargs} \n"
                    print(log_mes)
            return result
        return inner
    return wrapper


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x * y

print(my_function(3, 2))
