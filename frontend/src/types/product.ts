/**
 * ## Shadow interface of `backend/scripts/products.py`
 * A product in store has several properties:
 * - Name
 * - Price
 * - Category
 * - Image of the product
 */
export interface Product {
  name: string
  description: string
  price: number
  category: string
  image: string
}
