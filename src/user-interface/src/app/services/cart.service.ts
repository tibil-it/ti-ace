import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  cartItems: any[] = [];

  constructor() { }

  addCartItem(cartItem: any): void {
    if (this.cartItems.find(item => item.id === cartItem.id)) {
      return;
    }

    this.cartItems.push(cartItem);
  }

  removeCartItems(): void {
    this.cartItems = [];
  }
}
