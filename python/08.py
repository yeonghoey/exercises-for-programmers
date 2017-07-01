# -*- coding: utf-8 -*-
import fire


def main():
    num_people = number('How many people? ')
    num_pizza = number('How many pizzas do you have? ')
    num_slice = number('How many slices per pizza? ')

    total_slice = num_pizza * num_slice
    served_each = total_slice / num_people
    leftover = total_slice % num_people

    print 'Each person gets %d pieces of pizza.' % served_each
    print 'There are %d leftover pieces' % leftover


def number(message):
    s = raw_input(message)
    return int(s)


if __name__ == '__main__':
    fire.Fire()
