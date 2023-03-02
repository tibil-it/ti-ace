import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(private readonly router: Router) { }

  isUserLoggedIn(): boolean {
    return this.getUserDetails() && this.getUserDetails() !== 'undefined' && this.getUserDetails() !== 'null';
  }

  getUserDetails(): any {
    return JSON.parse(localStorage.getItem('userDetails') as string);
  }

  setUserDetails(userDetails: any, root = true): void {
    localStorage.setItem('userDetails', JSON.stringify(userDetails));
    if (root) {
      this.goToRootPage();
    }
  }

  goToRootPage(): void {
    this.router.navigate(['/aware']);
  }

  onLogout(): void {
    localStorage.removeItem('userDetails');
    this.router.navigate(['/auth/login']);
  }
}
