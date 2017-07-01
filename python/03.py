# -*- coding: utf-8 -*-
import fire


def main():
    quote = raw_input('What is the quote? ')
    who = raw_input('Who said it? ')
    print '%s says, "%s"' % (who, quote)


if __name__ == '__main__':
    fire.Fire()
