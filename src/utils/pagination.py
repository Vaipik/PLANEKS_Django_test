from typing import Iterable, Generator

from django.core.paginator import Page, Paginator


class PaginationMixin:

    def get_pages(self, **kwargs) -> dict:
        """Prettifying pagination view by sing elided page_range"""
        context = kwargs
        page: Page = context.get("page_obj")
        if page is not None:
            context.update(
                pages=page.paginator.get_elided_page_range(
                    number=page.number,
                    on_each_side=1,
                    on_ends=1
                )
            )

        return context


def get_paginator(request, objects: Iterable, per_page: int) -> tuple[Page, Generator]:
    """
    Function returns paginator object
    :param request: request
    :param objects: list of objects
    :param per_page: items per page
    :return: paginator object
    """
    paginator = Paginator(objects, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    pages = paginator.get_elided_page_range(
        number=page_number,
        on_each_side=1,
        on_ends=1
    )
    return page_obj, pages
