# -*- coding: utf-8 -*-

'''Wisielec
'''

HM_TEMPLATE = '''
 ------|
 |     |
 |     {0}
 |    {5}{1}{6}
 |     {2}
 |    {3} {4}
 |
/ \\
----------
'''

HM_PARTS = {
    0: 'O',
    1: '|',
    2: '|',
    3: '/',
    4: '\\',
    5: '/',
    6: '\\',
}


def print_gfx(fails):
    parts =  [' ' for fail in HM_PARTS.keys()]
    for fail in range(0, fails):
        if fail < fails:
            parts[fail] = HM_PARTS[fail]
    print(HM_TEMPLATE.format(*parts))


def main():
    for fails in range(8):
        print_gfx(fails)


if __name__ == '__main__':
    main()


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
