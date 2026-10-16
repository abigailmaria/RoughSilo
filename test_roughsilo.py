# test_roughsilo.py
"""
Tests for RoughSilo module.
"""

import unittest
from roughsilo import RoughSilo

class TestRoughSilo(unittest.TestCase):
    """Test cases for RoughSilo class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughSilo()
        self.assertIsInstance(instance, RoughSilo)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughSilo()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
