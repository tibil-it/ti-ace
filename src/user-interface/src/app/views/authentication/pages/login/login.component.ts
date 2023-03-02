import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  aadharNumber: any;
  entered = false;
  otp: any;

  constructor(private readonly authenticationService: AuthenticationService) {
    if (this.authenticationService.isUserLoggedIn()) {
      this.authenticationService.goToRootPage();
    }
  }

  ngOnInit(): void {
  }

  onLogin(): void {
    this.entered = true;
  }
  
  onEnterOTP(): void {
    this.authenticationService.setUserDetails({ id: this.aadharNumber });
    this.entered = true;
  }
}
