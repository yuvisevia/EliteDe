# test_defiminer.py
"""
Tests for DeFiMiner module.
"""

import unittest
from defiminer import DeFiMiner

class TestDeFiMiner(unittest.TestCase):
    """Test cases for DeFiMiner class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeFiMiner()
        self.assertIsInstance(instance, DeFiMiner)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeFiMiner()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
