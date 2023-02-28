import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AwareRoutingModule } from './aware-routing.module';
import { AwareComponent } from './aware.component';


@NgModule({
  declarations: [
    AwareComponent
  ],
  imports: [
    CommonModule,
    AwareRoutingModule
  ]
})
export class AwareModule { }
