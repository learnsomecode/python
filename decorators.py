def logan(func):
    def log(*args, **kwargs):
        print('Called {} with args {} and kwargs {}'.format(
            func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return log


@logan
def subtract(x, y, switch=False):
    return x - y if not switch else y - x

subtract(5, 2, switch=True)
