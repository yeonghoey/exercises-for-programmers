# -*- coding: utf-8 -*-
import fire


def main():
    noun = raw_input('Enter a noun: ')
    verb = raw_input('Enter a verb: ')
    adjective = raw_input('Enter an adjective: ')
    adverb = raw_input('Enter an adverb: ')
    print "Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!" \
           .format(**locals())


if __name__ == '__main__':
    fire.Fire()
