import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AspireComponent } from './aspire.component';

const routes: Routes = [{
  path: '',
  component: AspireComponent
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AspireRoutingModule { }
