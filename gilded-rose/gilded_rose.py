# -*- coding: utf-8 -*-

MAX_QUALITY = 50


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.quality >= MAX_QUALITY:
                continue

            quality_delta = -1
            if item.name == "Aged Brie":
                quality_delta = 1
            elif item.name == "Sulfuras, Hand of Ragnaros":
                quality_delta = 0

            if (
                item.name != "Backstage passes to a TAFKAL80ETC concert"
                and not item.name.startswith("Conjured")
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        quality_delta = -1
            elif item.name.startswith("Conjured"):
                if item.quality > 0:
                    quality_delta = -2
            else:
                if item.quality < MAX_QUALITY:
                    quality_delta = 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < MAX_QUALITY:
                                quality_delta += 1
                        if item.sell_in < 6:
                            if item.quality < MAX_QUALITY:
                                quality_delta += 1
            item.quality += quality_delta
            if item.quality < 0:
                item.quality = 0

            self.update_sell_in(item)
            if item.sell_in < 0:  # past sell by date
                if item.name != "Aged Brie":
                    if item.name.startswith("Conjured"):
                        if item.quality > 0:
                            item.quality = item.quality - 2
                    elif item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < MAX_QUALITY:
                        item.quality = item.quality + 1

    def update_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
