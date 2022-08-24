import datetime as dt


def get_file_name():
    return f"{dt.date.today()}__{dt.datetime.now().time()}"
