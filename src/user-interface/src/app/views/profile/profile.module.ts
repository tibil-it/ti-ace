import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgMultiSelectDropDownModule } from 'ng-multiselect-dropdown';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { SharedModule } from 'src/app/shared/shared.module';

import { ProfileRoutingModule } from './profile-routing.module';
import { ProfileComponent } from './profile.component';
import { CartComponent } from './pages/cart/cart.component';
import { CheckoutComponent } from './pages/checkout/checkout.component';
import { ConfirmComponent } from './pages/confirm/confirm.component';
import { PaymentComponent } from './pages/payment/payment.component';
import { CreateUserProfileComponent } from './pages/create-user-profile/create-user-profile.component';


@NgModule({
  declarations: [
    ProfileComponent,
    CartComponent,
    CheckoutComponent,
    ConfirmComponent,
    PaymentComponent,
    CreateUserProfileComponent
  ],
  imports: [
    CommonModule,
    ProfileRoutingModule,
    SharedModule,
    NgMultiSelectDropDownModule.forRoot(),
    FormsModule, 
    ReactiveFormsModule
  ]
})
export class ProfileModule { }
