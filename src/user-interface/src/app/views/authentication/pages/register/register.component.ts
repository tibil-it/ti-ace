import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  aadharNumber: any;
  entered = false;
  otp: any;

  constructor(private readonly authenticationService: AuthenticationService, private readonly router: Router) {
    if (this.authenticationService.isUserLoggedIn()) {
      //this.authenticationService.goToRootPage();
    }
  }

  ngOnInit(): void {
  }

  onRegister(): void {
    this.entered = true;
  }
  
  onEnterOTP(): void {
    this.authenticationService.setUserDetails({ id: this.aadharNumber });
    this.entered = true;
    this.router.navigate(['/profile/create-user-profile']);
  }
}
