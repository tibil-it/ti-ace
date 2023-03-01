import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AbleRoutingModule } from './able-routing.module';
import { AbleComponent } from './able.component';
import { SharedModule } from 'src/app/shared/shared.module';


@NgModule({
  declarations: [
    AbleComponent
  ],
  imports: [
    CommonModule,
    AbleRoutingModule,
    SharedModule
  ]
})
export class AbleModule { }
