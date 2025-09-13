#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Göstərilən tuple-ların ölçüsünü iki elementli etmək
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Yalnız ilk iki elementi götürmək
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
