import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AssessRoutingModule } from './assess-routing.module';
import { AssessComponent } from './assess.component';
import { SharedModule } from 'src/app/shared/shared.module';

@NgModule({
  declarations: [
    AssessComponent
  ],
  imports: [
    CommonModule,
    AssessRoutingModule,
    SharedModule
  ]
})
export class AssessModule { }
