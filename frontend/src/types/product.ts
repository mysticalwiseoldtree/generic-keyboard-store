/**
 * ## Shadow interface of `backend/scripts/products.py`
 * A product in store has several properties:
 * - Name
 * - Price
 * - Brand
 * - Image of the product
 */
export interface Product {
  name: string;
  price: number;
  brand: string;
  image: string;
}
