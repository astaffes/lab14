#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func(type="max"):
    def calc(coll):
        if type == "max":
            elem = max(coll)
        if type == "min":
            elem = min(coll)
        return elem

    return calc


if __name__ == "__main__":
    type = input("Введите тип значения - min или max: ")
    print("Введите кортеж элементов: ")
    a = (int(i) for i in input().split())
    print(f"Результат работы функции: {func(type)(a)}")
