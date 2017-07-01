# -*- coding: utf-8 -*-
import fire


def main():
    s = raw_input('What is the input string? ')
    print '%s has %d characters' % (s, len(s))


if __name__ == '__main__':
    fire.Fire()
