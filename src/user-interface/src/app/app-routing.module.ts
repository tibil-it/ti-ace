import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './views/home/home.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'aware',
    loadChildren: () => import('./views/aware/aware.module').then(module => module.AwareModule)
  },
  {
    path: 'aspire',
    loadChildren: () => import('./views/aspire/aspire.module').then(module => module.AspireModule)
  },
  {
    path: 'auth',
    loadChildren: () => import('./views/authentication/authentication.module').then(module => module.AuthenticationModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
