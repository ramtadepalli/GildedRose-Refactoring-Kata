# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    '''def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1'''
    
    def update(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            self.update_quality(item)
            item.sell_in -= 1

            if item.sell_in < 0:
                self.update_expire(item)

    def update_quality(self, item):
        if item.name == "Aged Brie":
            self.increment_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes_item(item)
        else:
            self.decrement_quality(item)

    def update_expire(self, item):
        if item.name == "Aged Brie":
            self.increment_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        else:
            self.decrement_quality(item)

    def increment_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrement_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def update_backstage_passes_item(self, item):
        self.increment_quality(item)
        if item.sell_in < 11:
            self.increment_quality(item)
        if item.sell_in < 6:
            self.increment_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
