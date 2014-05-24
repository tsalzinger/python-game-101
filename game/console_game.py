__author__ = 'Thomas Scheinecker'

fieldSize = eval(input('Field size: '))
entryPoint = eval(input('Entry point: '))
basePoint = eval(input('Base point: '))
path = eval(input('Path: '))

print("fieldSize: {fieldSize}; entryPoint {entryPoint}; basePoint; path {path}".format(**locals()))