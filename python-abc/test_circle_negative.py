#!/usr/bin/env python3

from task_01_duck_typing import Circle

def test_circle_negative():
    try:
        # Negativ radius veririk
        circle_negative = Circle(radius=-5)
        # Buraya gəlməməlidir, əgər ValueError atılmazsa test başarısız olacaq
        assert False, "ValueError should have been raised"
    except ValueError as e:
        # ValueError gözlənilir və mesajın uyğun olduğunu yoxlayırıq
        assert str(e) == "Radius cannot be negative", f"Unexpected error message: {e}"

# Testi işə salırıq
test_circle_negative()
