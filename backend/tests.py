"""
Tests for modules.
"""

import modules.product
from modules.product_database import ProductDatabase


### Start of Database tests ###
db = ProductDatabase()


def test_add_entry():
    product = modules.product.Product(
        "Test Product",
        "Test Description",
        100,
        "Test Category",
        "test_image.png",
        "test_uniqueid",
    )
    db.add_entry(product)
    result = db.read_entry(product)
    assert result == (
        "Test Product",
        "Test Description",
        100.0,
        "Test Category",
        "test_image.png",
        "test_uniqueid",
    )
    db.remove_entry(product)


def test_read_entry():
    product = modules.product.Product(
        "Test Product",
        "Test Description",
        100,
        "Test Category",
        "test_image.png",
        "test_uniqueid",
    )
    db.add_entry(product)
    result = db.read_entry(product)
    assert result == (
        "Test Product",
        "Test Description",
        100.0,
        "Test Category",
        "test_image.png",
        "test_uniqueid",
    )
    db.remove_entry(product)


def test_update_entry():
    product = modules.product.Product(
        "Test Product",
        "Test Description",
        100,
        "Test Category",
        "test_image.png",
        "test_uniqueid",
    )
    db.add_entry(product)
    product.name = "Updated Product"
    db.update_entry(product)
    result = db.read_entry(product)
    assert result == (
        "Updated Product",
        "Test Description",
        100.0,
        "Test Category",
        "test_image.png",
        "test_uniqueid",
    )
    db.remove_entry(product)


def test_remove_entry():
    product = modules.product.Product(
        "Test Product",
        "Test Description",
        100,
        "Test Category",
        "test_image.png",
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
