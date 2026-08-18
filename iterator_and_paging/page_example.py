END_OF_PAGE = object()

page1_ = [1,2,3,4, END_OF_PAGE]
page2_ = [5,6,7,8, END_OF_PAGE]


pages = [page1_, page2_]

class Page:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        for item in self.items:
            if item is END_OF_PAGE:
                return StopIteration("End of page")
            yield item




class PagedResult:
    def __init__(self, pages: list[Page]):
        self.pages = pages


    def __iter__(self):
        for page in self.pages:
            yield from page
        return StopIteration("End of paging")


def main():
    page1 = Page(page1_)
    page2 = Page(page2_)
    pages = [page1, page2]

    # chaining the two pages into a single iterable
    # for i in itertools.chain.from_iterable(pages):
    #     print(i)
    paged_result = PagedResult(pages)

    for item in paged_result:
        print(item)

if __name__ == "__main__":
    main()


def test_when_two_paged_result_is_iterated_then_returns_combination_of_two_lists():
    page1 = Page(page1_)
    page2 = Page(page2_)
    pages = [page1, page2]
    paged_result = PagedResult(pages)
    result = [v for v in paged_result]
    assert result == [1,2,3,4,5,6,7,8]
