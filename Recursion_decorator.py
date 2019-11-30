from functools import wraps


def memoization(func):
    # 缓存装饰器
    cache = {}
    miss = object()

    @wraps(func)
    def wrapper(args):
        result = cache.get(args, miss)
        if result is miss:
            result = func(args)
            cache[args] = result
        return result

    return wrapper


@memoization
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(9))