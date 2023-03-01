import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AssessRoutingModule } from './assess-routing.module';
import { AssessComponent } from './assess.component';

@NgModule({
  declarations: [
    AssessComponent
  ],
  imports: [
    CommonModule,
    AssessRoutingModule
  ]
})
export class AssessModule { }
