import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(private readonly router: Router) { }

  isUserLoggedIn(): boolean {
    return true;
  }

  getUserDetails(): any {
    return {
      name: 'Ram'
    };
  }

  goToRootPage(): void {
    this.router.navigate(['/aware']);
  }
}
