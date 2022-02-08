# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item(name="foo", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_foo_degradation_doubles(self):
        items = [Item(name="foo", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].quality)

    def test_foo_quality_never_negative(self):
        items = [Item(name="foo", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_aged_brie_quality_increases(self):
        items = [Item(name="Aged Brie", sell_in=1, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_max_quality(self):
        items = [Item(name="Aged Brie", sell_in=1, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_sulfuras_quality(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_backstage_passes(self):
        items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=0
            )
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

        gilded_rose.update_quality()  # 9 days left
        self.assertEquals(3, items[0].quality)

        gilded_rose.update_quality()  # 8 days left
        gilded_rose.update_quality()  # 7 days left
        gilded_rose.update_quality()  # 6 days left
        self.assertEquals(9, items[0].quality)
        self.assertEqual(6, items[0].sell_in)

        gilded_rose.update_quality()  # 5 days left
        self.assertEquals(11, items[0].quality)
        self.assertEquals(5, items[0].sell_in)

        gilded_rose.update_quality()  # 4 days left
        self.assertEquals(14, items[0].quality)
        self.assertEquals(4, items[0].sell_in)

        gilded_rose.update_quality()  # 3 days left
        gilded_rose.update_quality()  # 2 days left
        gilded_rose.update_quality()  # 1 day left
        gilded_rose.update_quality()  # 0 day left  (concert)
        gilded_rose.update_quality()  # -1 day left
        self.assertEquals(0, items[0].quality)

    def test_conjured_item(self):
        items = [Item(name="Conjured Foo", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)
        self.assertEquals(0, items[0].sell_in)

        gilded_rose.update_quality()
        self.assertEquals(4, items[0].quality)
        self.assertEquals(-1, items[0].sell_in)


if __name__ == "__main__":
    unittest.main()
