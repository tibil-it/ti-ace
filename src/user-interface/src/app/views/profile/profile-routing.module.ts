import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CartComponent } from './pages/cart/cart.component';
import { ConfirmComponent } from './pages/confirm/confirm.component';
import { CreateUserProfileComponent } from './pages/create-user-profile/create-user-profile.component';
import { PaymentComponent } from './pages/payment/payment.component';
import { ProfileComponent } from './profile.component';

const routes: Routes = [
  {
    path: '',
    component: ProfileComponent,
    children: [
      {
        path: 'cart',
        component: CartComponent
      },
      {
        path: 'confirm-order',
        component: ConfirmComponent
      },
      {
        path: 'payment',
        component: PaymentComponent
      },
      {
        path: 'create-user-profile',
        component: CreateUserProfileComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProfileRoutingModule { }
