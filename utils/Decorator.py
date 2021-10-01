# TODO Commenter le code


def deprecated(func):
    def wrapper(*args, **kwargs):
        print(
            f"[Warning] The function {func.__name__} is deprecated. Please consider using greedy_search() or a_star_search()"
        )

    return wrapper
