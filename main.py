#!/usr/bin/env python3

from logs import *

if __name__ == '__main__':
    section('Hello World')
    task('Print numbers')
    items(['one', 'two', 'three'])
    task('Some info', warn=True)
    step('I was walking in the rain')
    info('Then I was wet')

    for i in range(0, 100, 10):
        progress(i, i)
