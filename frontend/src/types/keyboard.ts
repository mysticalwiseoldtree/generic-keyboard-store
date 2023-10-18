/**
 * ## Shadow interface of `backend/scripts/keyboards.py`
 * A keyboard product in store has several properties:
 * - Name
 * - Price
 * - Brand
 * - Image of the product
 * - Switch type
 */
export interface Keyboard {
  name: string;
  price: number;
  brand: string;
  image: string;
  switch_type: string;
}
