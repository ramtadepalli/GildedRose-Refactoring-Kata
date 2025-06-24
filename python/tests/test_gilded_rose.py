# -*- coding: utf-8 -*-

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        print("This Is Sample Unit Test Method")
        items = [Item("Aged Brie", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEqual("Aged Brie", items[0].name)
    
    def test_backstage_pass_increases_quality(self):
        print("This Is Sample Unit Test Case test_backstage_pass_increases_quality Method")
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEqual(31, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

    def test_multiple_items(self):
        print("This Is Sample Unit Test Case Of Adding Multiple Items To List Method")
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 30),Item("Aged Brie", 20, 35),Item("Sulfuras, Hand of Ragnaros", 25, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEqual(36, items[1].quality)
        self.assertEqual(21, items[1].sell_in)
        
if __name__ == '__main__':
    unittest.main()
