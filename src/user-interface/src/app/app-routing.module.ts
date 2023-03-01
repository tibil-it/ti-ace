import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthenticationGuard } from './guards/authentication.guard';
import { LayoutComponent } from './layout/layout.component';
import { HomeComponent } from './views/home/home.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: '',
    component: LayoutComponent,
    canActivate: [AuthenticationGuard],
    children: [
      {
        path: 'aware',
        loadChildren: () => import('./views/aware/aware.module').then(module => module.AwareModule),
        canLoad: [AuthenticationGuard]
      },
      {
        path: 'aspire',
        loadChildren: () => import('./views/aspire/aspire.module').then(module => module.AspireModule),
        canLoad: [AuthenticationGuard]
      },
      {
        path: 'profile',
        loadChildren: () => import('./views/profile/profile.module').then(module => module.ProfileModule),
        canLoad: [AuthenticationGuard]
      },
      {
        path: 'assess',
        loadChildren: () => import('./views/assess/assess.module').then(module => module.AssessModule),
        canLoad: [AuthenticationGuard]
      },
      {
        path: 'able',
        loadChildren: () => import('./views/able/able.module').then(module => module.AbleModule),
        canLoad: [AuthenticationGuard]
      },
      {
        path: 'access',
        loadChildren: () => import('./views/access/access.module').then(module => module.AccessModule),
        canLoad: [AuthenticationGuard]
      }
    ]
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
