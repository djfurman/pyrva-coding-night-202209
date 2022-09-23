# https://codingdojo.org/kata/PaginationSeven/

from app.project import get_pagination
import pytest


def it_shows(result: list[str], page: int) -> str:
    return result[page - 1]


def result_as_string(result) -> str:
    return " ".join(result)


def test_it_shows_page_2_of_5() -> None:
    """
    First of all, we need to represent all pages until 7,
    the goal is to show the current page between ( and ), as examples:

    Page 2 of 5:

    1 (2) 3 4 5"""
    # Arrange (Given)
    page = 2
    max_pages = 5
    # Act (When)
    result = get_pagination(page, max_pages)
    # Assert (Then)
    print(result)
    assert it_shows(result, page) == "(2)"


@pytest.mark.parametrize(
    "page, max_pages, expected",
    [
        # Part I
        (2, 5, "1 (2) 3 4 5"),
        (3, 5, "1 2 (3) 4 5"),
        (6, 7, "1 2 3 4 5 (6) 7"),
        # Part II
        (42, 100, "1 … 41 (42) 43 … 100"),
        (5, 9, "1 … 4 (5) 6 … 9"),
        # Part III
        (1, 9, "(1) 2 3 4 5 … 9"),
        (2, 9, "1 (2) 3 4 5 … 9"),
        (3, 9, "1 2 (3) 4 5 … 9"),
        (4, 9, "1 2 3 (4) 5 … 9"),
        # Part IV
        (6, 9, "1 … 5 (6) 7 8 9"),
        (7, 9, "1 … 5 6 (7) 8 9"),
        (8, 9, "1 … 5 6 7 (8) 9"),
        (9, 9, "1 … 5 6 7 8 (9)"),
    ],
)
def test_it_shows(page, max_pages, expected):
    result = get_pagination(page=page, max_pages=max_pages)
    assert result_as_string(result) == expected
