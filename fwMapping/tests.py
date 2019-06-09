from django.test import TestCase

# # Create your tests here.
# a =1
# b = 2
# c= a if a>1 else b  #如果a大于1的话，c=a，否则c=b
#
# print(c)
# xxx_dic ={"lanip": "192.168.1.5", "csrfmiddlewaretoken": "D7n97SDJmvHtiB72FHQfEaehiZ8ym1EsNlLxXzuK6KcwvBo8Dqxz5Un7q8AuCQWP", "id": "11"}
# print(xxx_dic.pop("id"))

# def addddd():
#     if a > 2:
#         a = 1
#     else:
#         a = 2
#     return a
#
# a= addddd()
# print(a)
# a=1
# print(isinstance(a,int))

import os
import django
from django.core import paginator

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'managePlatform.settings')
    django.setup()

    from fwMapping import models
    mapp_list = models.Mapping.objects.all().order_by('pk')
    page = paginator.Paginator(mapp_list, 3)
    print(page.num_pages)
    print(page.page_range)
    # current = page.page(2)
    # print(current.object_list)
    # print(current.has_next())
    # print(current.next_page_number())
    # print(current.has_previous())
    # print(current.previous_page_number())

