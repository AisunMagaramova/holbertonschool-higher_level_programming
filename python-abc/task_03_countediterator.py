#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Iteratora çevrilən obyekt
        self.count = 0  # Iterasiya sayğacı

    def __next__(self):
        try:
            item = next(self.iterator)  # Növbəti element alırıq
            self.count += 1  # Sayğacı artırırıq
            return item
        except StopIteration:
            raise StopIteration  # Element qalmadıqda StopIteration atılır

    def get_count(self):
        return self.count  # Sayğacın cari dəyəri
