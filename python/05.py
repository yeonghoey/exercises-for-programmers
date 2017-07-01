# -*- coding: utf-8 -*-
import fire


def main():
    a = raw_input('What is the first number? ')
    b = raw_input('What is the first number? ')
    a, b = int(a), int(b)
    print '%d + %d = %d' % (a, b, a+b)
    print '%d - %d = %d' % (a, b, a-b)
    print '%d * %d = %d' % (a, b, a*b)
    print '%d / %d = %d' % (a, b, a/b)


if __name__ == '__main__':
    fire.Fire()
