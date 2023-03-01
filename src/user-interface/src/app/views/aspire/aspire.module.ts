import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SharedModule } from 'src/app/shared/shared.module';

import { AspireRoutingModule } from './aspire-routing.module';
import { AspireComponent } from './aspire.component';


@NgModule({
  declarations: [
    AspireComponent
  ],
  imports: [
    CommonModule,
    AspireRoutingModule,
    SharedModule
  ]
})
export class AspireModule { }
