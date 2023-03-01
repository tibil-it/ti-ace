import { Component, OnInit } from '@angular/core';
import { faShoppingCart, faUserCircle } from '@fortawesome/free-solid-svg-icons';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  faShoppingCart = faShoppingCart;
  faUserCircle = faUserCircle;

  constructor(public readonly cartService: CartService) { }

  ngOnInit(): void {
  }

}
