# -*- coding: utf-8 -*-
import fire


#: Unit Conversion Factor from squre feet to squre meters
F2M2_FACTOR = 0.09290304


def main():
    lfeet = number('What is the length of the room in feet? ')
    wfeet = number('What is the width of the room in feet? ')

    print 'You entered dimensions of %d feet by %d feet.' % (lfeet, wfeet)
    area_f2 = lfeet * wfeet
    area_m2 = area_f2 * F2M2_FACTOR
    print 'The area is %d square feet, %.3f square meters' % (area_f2, area_m2)


def number(message):
    s = raw_input(message)
    return int(s)


if __name__ == '__main__':
    fire.Fire()
