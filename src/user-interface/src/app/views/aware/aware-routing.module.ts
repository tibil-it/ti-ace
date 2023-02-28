import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AwareComponent } from './aware.component';

const routes: Routes = [{
  path: '',
  component: AwareComponent
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AwareRoutingModule { }
