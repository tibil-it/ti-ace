import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private readonly authenticationService: AuthenticationService) {
    if (this.authenticationService.isUserLoggedIn()) {
      this.authenticationService.goToRootPage();
    }
  }

  ngOnInit(): void {
  }

}
