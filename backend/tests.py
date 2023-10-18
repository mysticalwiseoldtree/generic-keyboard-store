"""
Tests for modules.
"""

import modules.keyboards
from modules.product_database import ProductDatabase


### Start of Database tests ###
db = ProductDatabase()


def test_add_entry():
    product = modules.keyboards.Keyboard(
        "Test Keyboard",
        100,
        "Test Brand",
        "test_image.png",
        "Test Switch",
        "test_uniqueid",
    )
    db.add_entry(product)
    result = db.read_entry(product)
    assert result == (
        "Test Keyboard",
        100.0,
        "Test Brand",
        "test_image.png",
        "Test Switch",
        "test_uniqueid",
    )
    db.remove_entry(product)


def test_read_entry():
    product = modules.keyboards.Keyboard(
        "Test Keyboard",
        100,
        "Test Brand",
        "test_image.png",
        "Test Switch",
        "test_uniqueid",
    )
    db.add_entry(product)
    result = db.read_entry(product)
    assert result == (
        "Test Keyboard",
        100.0,
        "Test Brand",
        "test_image.png",
        "Test Switch",
        "test_uniqueid",
    )
    db.remove_entry(product)


def test_update_entry():
    product = modules.keyboards.Keyboard(
        "Test Keyboard",
        100,
        "Test Brand",
        "test_image.png",
        "Test Switch",
        "test_uniqueid",
    )
    db.add_entry(product)
    product.name = "Updated Keyboard"
    db.update_entry(product)
    result = db.read_entry(product)
    assert result == (
        "Updated Keyboard",
        100.0,
        "Test Brand",
        "test_image.png",
        "Test Switch",
        "test_uniqueid",
    )
    db.remove_entry(product)


def test_remove_entry():
    product = modules.keyboards.Keyboard(
        "Test Keyboard",
        100,
        "Test Brand",
        "test_image.png",
        "Test Switch",
        "test_uniqueid",
    )
    db.add_entry(product)
    db.remove_entry(product)
    result = db.read_entry(product)
    assert result == None


def test_database():
    test_add_entry()
    test_read_entry()
    test_update_entry()
    test_remove_entry()


### End of Database tests ###


if __name__ == "__main__":
    test_database()
    print("All tests passed!")
