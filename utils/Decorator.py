
# Simple décorateur personnalisé afin de savoir si une ancienne fonction est utilisée ou non
def deprecated(func):
    def wrapper(*args, **kwargs):
        print(
            f"[Warning] The function {func.__name__} is deprecated. Please consider using greedy_search() or a_star_search()"
        )

    return wrapper
