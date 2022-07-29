from termcolor import colored


def info(*args, **kwargs):
    print('  ', *args, **kwargs)


def section(name, warn=False):
    print(colored('==>', 'yellow' if warn else 'green'), colored(name, 'white', attrs=['bold']))


def step(name, warn=False):
    print(colored(' ->', 'yellow' if warn else 'blue'), colored(name, 'white', attrs=['bold']))


def items(data, warn=False):
    for i, text in enumerate(data):
        print(colored('::', 'yellow' if warn else 'blue'), f'({i}/{len(data)})', text)
