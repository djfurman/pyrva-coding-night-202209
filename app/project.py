# https://codingdojo.org/kata/PaginationSeven/

SPAN = "…"


def get_pagination(page: int, max_pages: int) -> list[str]:
    if not 1 <= page <= max_pages:
        raise ValueError(f"Page must be between 0 and {max_pages}, got {page}")

    ix = page - 1

    pagination = [1, SPAN, page - 1, f"({page})", page + 1, SPAN, max_pages]

    if max_pages <= 7:
        pagination = [page for page in range(1, max_pages + 1)]
        pagination[ix] = f"({pagination[ix]})"

    elif page <= 4:
        pagination[:5] = [1, 2, 3, 4, 5]
        pagination[ix] = f"({pagination[ix]})"

    elif max_pages - page < 4:
        pagination[2:] = [p for p in range(max_pages - 4, max_pages + 1)]
        ix = 7 - (max_pages - page) - 1
        pagination[ix] = f"({pagination[ix]})"

    return [str(page) for page in pagination]
