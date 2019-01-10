from django.test import TestCase
import bs4
def testyield():
    yield 1
    yield 2

if __name__ == '__main__':
    for i in testyield():
        print(i)