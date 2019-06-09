from django.core import paginator

class Paginator_page(object):
    def __init__(self, request, queryset, page_num):
        self.request = request
        self.queryset = queryset
        self.page_num = page_num

    @property
    def get_page(self):
        paginators = paginator.Paginator(self.queryset, self.page_num)
        try:
            # 第N行
            current_page_num = int(self.request.GET.get("page"))
            if current_page_num > paginators.num_pages:
                current_page_num = 1
            elif current_page_num <= 0:
                current_page_num = 1
        except Exception:
            current_page_num = 1

        # 循环值的时候应当打印它, 显示每行有多少个
        current_page = paginators.page(current_page_num)

        if paginators.num_pages > 11:
            if current_page_num - 5 < 1:
                paginator_range = range(1, 12)
            elif current_page_num + 6 > paginators.num_pages:
                # 左边-10右边+1
                paginator_range = range(paginators.num_pages - 10, paginators.num_pages + 1)
            else:
                paginator_range = range(current_page_num - 5, current_page_num + 6)
        else:
            # 获取总共有多少行 range(x, x)
            paginator_range = paginators.page_range
        return {"queryset": current_page, "paginator_range": paginator_range,
                "current_page_num": current_page_num}