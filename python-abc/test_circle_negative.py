#!/usr/bin/env python3

import unittest
from task_01_duck_typing import Circle

class TestCircle(unittest.TestCase):
    
    def test_negative_radius(self):
        """Test that Circle raises ValueError for negative radius."""
        with self.assertRaises(ValueError) as context:
            Circle(radius=-5)
        
        # Bu sətir testin düzgün işləyişi üçün lazımdır
        self.assertEqual(str(context.exception), "Radius cannot be negative")

# Testi işə salırıq
if __name__ == '__main__':
    unittest.main()
