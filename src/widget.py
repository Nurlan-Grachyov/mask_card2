import masks

data = str(input())


def get_date(date: str) -> str:
    """Определяем дату"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date(data))
