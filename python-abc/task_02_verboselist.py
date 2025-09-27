#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            item = super().pop()  # Sonuncu elementi pop edir
            print(f"Popped [{item}] from the list.")
            return item  # Elementi qaytarırıq
        else:
            item = super().pop(index)  # İstədiyiniz indeksdən pop edir
            print(f"Popped [{item}] from the list.")
            return item
