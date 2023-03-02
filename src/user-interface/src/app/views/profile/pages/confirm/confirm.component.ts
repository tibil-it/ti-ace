import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AspireService } from 'src/app/services/aspire.service';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-confirm',
  templateUrl: './confirm.component.html',
  styleUrls: ['./confirm.component.scss']
})
export class ConfirmComponent implements OnInit {

  cartItems: any;
  totalPrice = 0;

  constructor(private readonly cartService: CartService, private readonly aspireService: AspireService, private readonly _router: Router, private toastr: ToastrService) {
    this.cartItems = this.cartService.cartItems;
    this.cartItems.forEach((cartItem: any) => this.totalPrice += cartItem.price);
  }

  ngOnInit(): void {
  }

  onConfirmOrder(): void {
    this.aspireService.initItems(this.cartItems).subscribe((res: any) => {
      this._router.navigate(['/profile/payment']);
    }, error => {
      this.toastr.error('Oops!', 'Something went wrong!', {
        positionClass: 'toast-bottom-center',
        timeOut: 500
      });
      this._router.navigate(['/profile/payment']);
    });
  }

}
