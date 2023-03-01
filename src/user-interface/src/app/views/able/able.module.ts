import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AbleRoutingModule } from './able-routing.module';
import { AbleComponent } from './able.component';


@NgModule({
  declarations: [
    AbleComponent
  ],
  imports: [
    CommonModule,
    AbleRoutingModule
  ]
})
export class AbleModule { }
