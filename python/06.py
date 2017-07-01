# -*- coding: utf-8 -*-
from datetime import datetime
import fire


def main():
    current_age = number('What is your current age? ')
    retire_age = number('At what age would you like to retire? ')

    remaining = retire_age - current_age
    this_year = datetime.now().year
    retire_year = this_year + remaining

    print 'You have %d yeras left until you can retire' % remaining
    print "It's %d, so you can retire in %d" % (this_year, retire_year)


def number(message):
    s = raw_input(message)
    return int(s)


if __name__ == '__main__':
    fire.Fire()
