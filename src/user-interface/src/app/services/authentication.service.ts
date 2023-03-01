import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  userDetails: any;

  constructor(private readonly router: Router) { }

  isUserLoggedIn(): boolean {
    return true;
  }

  getUserDetails(): any {
    return this.userDetails;
  }

  setUserDetails(userDetails: any): void {
    this.userDetails = userDetails;
    this.goToRootPage();
  }

  goToRootPage(): void {
    this.router.navigate(['/aware']);
  }
}
