import { Component, OnInit } from '@angular/core';
import { faShoppingCart, faUserCircle } from '@fortawesome/free-solid-svg-icons';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  faShoppingCart = faShoppingCart;
  faUserCircle = faUserCircle;
  cartCount = 0;

  constructor(public readonly cartService: CartService, private readonly authService: AuthenticationService) { }

  ngOnInit(): void {
    this.cartService.cartItems.subscribe(items => {
      console.log(items);
      this.cartCount = items.length;
    })
  }

  logout(): void {
    this.authService.onLogout();
  }

}
