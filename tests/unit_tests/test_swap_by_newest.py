import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_nominal_case():
    # Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=15)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=3)
    item_e = Decor(age=10)
    item_f = Clothing(age=9)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_d in tai.inventory

def test_swap_by_newest_empty_self_inventory():
    # Arrange
    # me
    tai = Vendor(
        inventory=[]
    )

    # them
    item_d = Clothing(age=3)
    item_e = Decor(age=10)
    item_f = Clothing(age=9)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    assert not result
    assert len(tai.inventory) == 0
    assert jesse.inventory == [item_d, item_e, item_f]

def test_swap_by_newest_empty_other_inventory():
    # Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=15)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    assert not result
    assert len(jesse.inventory) == 0
    assert tai.inventory == [item_a, item_b, item_c]

def test_swap_by_newest_duplicate_age_swaps_first():
    # Arrange
    # me
    item_a = Decor(age=15)
    item_b = Electronics(age=2)
    item_c = Decor(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=30)
    item_e = Decor(age=10)
    item_f = Clothing(age=10)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in tai.inventory

