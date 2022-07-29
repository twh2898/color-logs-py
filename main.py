#!/usr/bin/env python3

import logs as l

if __name__ == '__main__':
    l.section('Hello World')
    l.step('Print numbers')
    l.items(['one', 'two', 'three'])
    l.section('Some info', warn=True)
    l.info('I was walking in the rain')
    l.info('Then I was wet')
