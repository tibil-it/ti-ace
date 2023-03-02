import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  cartItems: any[] = [];

  constructor(private toastr: ToastrService) { }

  addCartItem(cartItem: any): void {
    if (this.cartItems.find(item => item.id === cartItem.id)) {
      return;
    }

    this.cartItems.push(cartItem);
    this.toastr.success('', 'Item added to your cart', {
      positionClass: 'toast-bottom-center',
      timeOut: 500
    });
  }

  removeCartItems(): void {
    this.cartItems = [];
  }
}
