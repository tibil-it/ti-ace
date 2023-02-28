import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AspireRoutingModule } from './aspire-routing.module';
import { AspireComponent } from './aspire.component';


@NgModule({
  declarations: [
    AspireComponent
  ],
  imports: [
    CommonModule,
    AspireRoutingModule
  ]
})
export class AspireModule { }
