from django.test import TestCase

# Create your tests here.
a =1
b = 2
c= a if a>1 else b  #如果a大于1的话，c=a，否则c=b

print(c)
