import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  cartItems: BehaviorSubject<any> = new BehaviorSubject<any>(this.getLocalCartProducts() || []);

  constructor(private toastr: ToastrService) { }

  addCartItem(cartItem: any): void {
    let cartItems = this.getLocalCartProducts() || [];
    if (cartItems.find((item: any) => item.id === cartItem.id)) {
      return;
    }

    cartItems.push(cartItem);
    this.setCartProductsLocally(cartItems);
    this.cartItems.next(cartItems);

    this.toastr.success('', 'Item added to your cart', {
      positionClass: 'toast-bottom-center',
      timeOut: 500
    });
  }

  removeCartItems(): void {
    this.removeLocalCartProducts();
    this.cartItems.next([]);
  }

  setCartProductsLocally(cartItems: any): void {
    this.removeLocalCartProducts();
    localStorage.setItem('cart-items', JSON.stringify(cartItems));
  }

  getLocalCartProducts(): any {
    return JSON.parse(localStorage.getItem('cart-items') as string);
  }

  removeLocalCartProducts(): any {
    localStorage.removeItem('cart-items');
  }
}
