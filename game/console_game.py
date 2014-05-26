__author__ = 'Thomas Scheinecker'

from field import Field
from base_entity import BaseEntity

fieldSize = eval(input('Field size: '))
entryPoint = eval(input('Entry point: '))
basePoint = eval(input('Base point: '))
path = eval(input('Path: '))

print("fieldSize: {fieldSize}; entryPoint {entryPoint}; basePoint; path {path}".format(**locals()))

base = BaseEntity(100, 0, "BASE", "Your base", basePoint, 2, 3, 5, (2, 2))

print(base)

field = Field(path, fieldSize, entryPoint, base)

print(field)