from django.test import TestCase

# Create your tests here.


a = [{'client': '客户端1', 'score': 999999}, {'client': '客户端2', 'score': 88888}, {'client': '客户端3', 'score': 77777}, {'client': '客户端4', 'score': 66666}, {'client': '客户端5', 'score': 77777}, {'client': '客户端6', 'score': 6666}, {'client': '客户端7', 'score': 123}, {'client': '客户端8', 'score': 0}, {'client': '客户端5', 'score': 12345678}]
print(a)
result = sorted(a,  key=lambda x:x['score'])