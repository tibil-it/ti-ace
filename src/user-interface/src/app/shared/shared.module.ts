import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { BasicCardComponent } from './components/cards/basic-card/basic-card.component';
import { SearchBarComponent } from './components/search-bar/search-bar.component';
import { BasicHorizontalCardComponent } from './components/cards/basic-horizontal-card/basic-horizontal-card.component';

const DECLARATIONS = [
  BasicCardComponent,
  SearchBarComponent,
  BasicHorizontalCardComponent
];

@NgModule({
  declarations: [
    DECLARATIONS
  ],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    DECLARATIONS
  ]
})
export class SharedModule { }
