from termcolor import colored


def section(text):
    print(colored('::', 'blue'), colored(text, 'white', attrs=['bold']))


def task(text, warn=False):
    print(colored('==>', 'yellow' if warn else 'green'),
          colored(text, 'white', attrs=['bold']))


def step(text, warn=False):
    print(colored(' ->', 'yellow' if warn else 'blue'),
          colored(text, 'white', attrs=['bold']))


def item(i, n, text):
    print(f'({i}/{n})', text)


def items(data):
    for i, text in enumerate(data):
        i += 1
        item(i, len(data), text)


def progress(perc, text):
    print(f'[{perc:3}%]', text)


def info(*args, **kwargs):
    print('  ', *args, **kwargs)
