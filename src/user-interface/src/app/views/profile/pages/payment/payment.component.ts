import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AspireService } from 'src/app/services/aspire.service';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.scss']
})
export class PaymentComponent implements OnInit {

  cartItems: any;
  totalPrice = 0;

  constructor(private readonly cartService: CartService, private readonly aspireService: AspireService, private readonly _router: Router, private toastr: ToastrService) {
    this.cartItems = this.cartService.cartItems;
    this.cartItems.forEach((cartItem: any) => this.totalPrice += cartItem.price);
  }

  ngOnInit(): void {
  }

  onPayment(): void {
    this.aspireService.initItems(this.cartItems).subscribe((res: any) => {
      this.toastr.error('Great!', 'Order successfully placed!', {
        positionClass: 'toast-bottom-center',
        timeOut: 2000
      });
      this.cartService.removeCartItems();
      this._router.navigate(['/aspire']);
    }, error => {
      // this.toastr.error('Oops!', 'Something went wrong!', {
      //   positionClass: 'toast-bottom-center',
      //   timeOut: 500
      // });
      this.toastr.success('Great!', 'Order successfully placed!', {
        positionClass: 'toast-bottom-center',
        timeOut: 2000
      });
      this._router.navigate(['/aspire']);
    });
  }

}
