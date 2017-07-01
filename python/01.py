# -*- coding: utf-8 -*-
import fire


def main():
    name = raw_input('What is your name? ')
    print 'Hello, %s, nice to meet you!' % name


def no_variables():
    print 'Hello, %s, nice to meet you!' % raw_input('What is your name? ')


if __name__ == '__main__':
    fire.Fire()
