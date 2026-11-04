import json
import sys
from field import field
from gen_random import gen_random
from print_result import print_result
from timer import cm_timer1, cm_timer2 
from unique import Unique


path = r"data_light.json" 

with open(path) as f:
    data = json.load(f)


@print_result
def f1(data):
    return sorted(list(Unique(field(data, "job-name"), ignore_case=True)), key = str.lower)

@print_result
def f2(arg):
    return list(filter(lambda c: c.lower().startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda p: f"{p} с опытом Python", arg))


@print_result
def f4(arg):
    cost = [x for x in gen_random(len(arg), 100000, 1000000)]
    pairs = zip(arg, cost)
    return list(map(lambda x: f"{x[0]}, зарплата {x[1]} рублей", pairs))


if __name__ == '__main__':
    with cm_timer1():
        f4(f3(f2(f1(data))))