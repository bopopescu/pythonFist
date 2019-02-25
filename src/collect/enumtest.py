#
# from enum import Enum
#
#
# class DuplicateFreeEnum(Enum):
#     def __init__(self, *args):
#         cls = self.__class__
#         if any(self.value == e.value for e in cls):
#             a = self.name
#             e = cls(self.value).name
#             raise ValueError("aliases not allowed in DuplicateFreeEnum: %r --> %r" % (a, e))
#
#
# class Color(DuplicateFreeEnum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#     GRENE = 2

# from enum import Enum
#
#
# class Planet(Enum):
#
#     MERCURY = (3.303e+23, 2.4397e6)
#     VENUS = (4.869e+24, 6.0518e6)
#     EARTH = (5.976e+24, 6.37814e6)
#     MARS = (6.421e+23, 3.3972e6)
#     JUPITER = (1.9e+27, 7.1492e7)
#     SATURN = (5.688e+26, 6.0268e7)
#     URANUS = (8.686e+25, 2.5559e7)
#     NEPTUNE = (1.024e+26, 2.4746e7)
#
#     def __init__(self, mass, radius):
#             self.mass = mass
#             self.radius = radius
#
#     @property
#     def surface_gravity(self):
#         G = 6.67300E-11
#         return G * self.mass / (self.radius * self.radius)
#
#
# print(Planet.EARTH.value)

#
# from datetime import timedelta
# from enum import Enum
#
#
# class Period(timedelta, Enum):
#     """different lengths of time"""
#     _ignore_ = 'Period i'
#     Period = vars()
#     for i in range(367):
#         Period['day_%' % i] = i
#
#
# print(list(Period)[:2])


# from enum import Enum
#
# class FieldTypes(Enum):
#     name = 0
#     value

# from decimal import Decimal, Context

# print(Decimal.from_float(0.1))
#
# print(Decimal.from_float(float('nan')))
# print(Decimal.from_float(float('inf')))
# print(Decimal.from_float(float('-inf')))
# print(Decimal(2).fma(3, 5))

# print(Decimal('1.41421356').quantize(Decimal('1.000')))
# print(Decimal(18).remainder_near(Decimal(10)))


# from decimal import Context, ROUND_DOWN
# import math
#
# context = Context(prec=6, rounding=ROUND_DOWN)
# print(context.create_decimal_from_float(math.pi))

# from fractions import Fraction
# print(Fraction('3.141592653589732').limit_denominator(1000))
# from math import floor
# from fractions import Fraction
#
# print(floor(Fraction(355, 113)))
# from random import random, uniform, expovariate, randrange, choice, shuffle, sample
#
# print(random())
# print(uniform(2.5, 10.0))
# print(expovariate(1 / 5))
# print(randrange(10))
# print(choice(['win', 'lose', 'draw']))
#
# deck = 'ace two three four'.split()
# shuffle(deck)
# print(deck)
#
# print(sample([10, 20, 30, 40, 50], k=4))

# from statistics import mean
# from random import shuffle
#
# drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
# placebo = [54, 51, 58, 44, 55, 52,42, 47, 58, 46]
# observed_diff = mean(drug) - mean(placebo)
#
# n = 10000
# count = 0
# combined = drug + placebo
# for i in range(n):
#     shuffle(combined)
#     new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
#     count += (new_diff >= observed_diff)
#
#
# print(f'{n} label reshufflings produced only {count} instances with difference')
#
# print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
# print(f'The one-sided p-value of{count / n:.4f} leads us to reject the null')
#



# from random import expovariate,gauss
# from statistics import mean, median,stdev
#
# average_arrival_interval = 5.6
# average_service_time = 5.0
# stdev_service_time = 0.5
#
# num_waiting = 0
# arrivals = []
# starts = []
# arrival = service_end = 0.0
#
# for i in range(20000):
#     if arrival <= service_end:
#         num_waiting += 1
#         arrival += expovariate(1.0 / average_arrival_interval)
#         arrivals.append(arrival)
#     else:
#         num_waiting -= 1
#         service_start = service_end if num_waiting else arrival
#         service_time = gauss(average_service_time, stdev_service_time)
#         starts.append(service_start)
#
# waits = [starts - arrival for arrival, start in zip(arrivals, starts)]
# print(f'Mean wait:{mean(waits):.1f}. Stdev wait:{stdev(waits):.1f}.')
from statistics import mean
from fractions import Fraction as F

# print(mean([1, 2, 3, 4, 4]))
# print(mean([-1.0, 2.5, 3.25, 5.75]))
# print(mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(mean([D()]))




























